"""
Kafka Provider is a class that allows to ingest/digest data from Grafana.
"""
import base64
import dataclasses
import datetime
import inspect
import logging
import os
import random

import pydantic
import requests

from keep.api.models.alert import AlertDto
from keep.contextmanager.contextmanager import ContextManager
from keep.providers.base.base_provider import BaseProvider
from keep.providers.models.provider_config import ProviderConfig, ProviderScope
from keep.providers.providers_factory import ProvidersFactory


@pydantic.dataclasses.dataclass
class DynatraceProviderAuthConfig:
    """
    Dynatrace authentication configuration.
    """

    environment_id: str = dataclasses.field(
        metadata={
            "required": True,
            "description": "Dynatrace's environment ID",
            "hint": "e.g. abcde",
        },
    )
    api_token: str = dataclasses.field(
        metadata={
            "required": True,
            "description": "Dynatrace's API token",
            "hint": "e.g. dt0c01.abcde...",
            "sensitive": True,
        },
    )
    alerting_profile: str = dataclasses.field(
        default="Default",
        metadata={
            "required": False,
            "description": "Dynatrace's alerting profile for the webhook integration. Defaults to 'Default'",
            "hint": "The name of the alerting profile to use for the webhook integration",
        },
    )


class DynatraceProvider(BaseProvider):
    """
    Dynatrace provider class.
    """

    PROVIDER_SCOPES = [
        ProviderScope(
            name="problems.read",
            description="Read access to Dynatrace problems",
            mandatory=True,
            alias="Problem Read",
        ),
        ProviderScope(
            name="settings.read",
            description="Read access to Dynatrace settings [for webhook installation]",
            mandatory=False,
            alias="Settings Read",
        ),
        ProviderScope(
            name="settings.write",
            description="Write access to Dynatrace settings [for webhook installation]",
            mandatory=False,
            alias="Settings Write",
        ),
    ]

    def __init__(
        self, context_manager: ContextManager, provider_id: str, config: ProviderConfig
    ):
        super().__init__(context_manager, provider_id, config)

    def _get_alerts(self) -> list[AlertDto]:
        """
        Get alerts from Dynatrace.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            list[AlertDto]: List of alerts.
        """
        self.logger.info("Getting alerts from Dynatrace")
        response = requests.get(
            f"https://{self.authentication_config.environment_id}.live.dynatrace.com/api/v2/problems",
            headers={
                "Authorization": f"Api-Token {self.authentication_config.api_token}"
            },
        )
        if not response.ok:
            self.logger.exception(
                f"Failed to get problems from Dynatrace: {response.text}"
            )
            raise Exception(f"Failed to get problems from Dynatrace: {response.text}")
        else:
            return [
                self.format_alert(event)
                for event in response.json().get("problems", [])
            ]

    def validate_scopes(self):
        self.logger.info("Validating dynatrace scopes")
        scopes = {}
        try:
            self._get_alerts()
        except Exception as e:
            # wrong environment
            if "Not Found" in str(e):
                self.logger.info(
                    f"Failed to validate dynatrace scopes - wrong environment id"
                )
                scopes[
                    "problems.read"
                ] = "Failed to validate scope, wrong environment id (Keep got 404)"
                scopes["settings.read"] = scopes["problems.read"]
                scopes["settings.write"] = scopes["problems.read"]
                return scopes
            # authentication
            if "401" in str(e):
                self.logger.info(
                    f"Failed to validate dynatrace scopes - invalid API token"
                )
                scopes[
                    "problems.read"
                ] = "Invalid API token - authentication failed (401)"
                scopes["settings.read"] = scopes["problems.read"]
                scopes["settings.write"] = scopes["problems.read"]
                return scopes
            if "403" in str(e):
                self.logger.info(
                    f"Failed to validate dynatrace scopes - no problems.read scopes"
                )
                scopes[
                    "problems.read"
                ] = "Token is missing required scope - problems.read (403)"
        else:
            self.logger.info(f"Validated dynatrace scopes - problems.read")
            scopes["problems.read"] = True

        # check webhook scopes:
        # settings.read:
        try:
            self._get_alerting_profiles()
            self.logger.info(f"Validated dynatrace scopes - settings.read")
            scopes["settings.read"] = True
        except Exception as e:
            self.logger.info(
                f"Failed to validate dynatrace scopes - settings.read: {e}"
            )
            scopes["settings.read"] = str(e)
            scopes[
                "settings.write"
            ] = "Cannot validate the settings.write scope without the settings.read scope, you need to first add the settings.read scope"
            # we are done
            return scopes
        # if we have settings.read, we can try settings.write
        try:
            self.logger.info(f"Validating dynatrace scopes - settings.write")
            keep_api_url = os.environ.get("KEEP_API_URL")
            self.setup_webhook(
                tenant_id=self.context_manager.tenant_id,
                keep_api_url=keep_api_url,
                api_key="TEST",
                setup_alerts=False,
            )
            scopes["settings.write"] = True
            self.logger.info(f"Validated dynatrace scopes - settings.write")
        except Exception as e:
            self.logger.info(
                f"Failed to validate dynatrace scopes - settings.write: {e}"
            )
            # understand if its localhost:
            if "The environment does not allow for site-local URLs" in str(e):
                scopes[
                    "settings.write"
                ] = "Cannot use localhost as a webhook URL, please use a public URL when installing dynatrace webhook (you can use Keep with ngrok or similar)"
            else:
                scopes[
                    "settings.write"
                ] = f"Failed to validate the settings.write scope: {e}"
            return scopes

        self.logger.info(f"Validated dynatrace scopes: {scopes}")
        return scopes

    @staticmethod
    def format_alert(event: dict) -> AlertDto:
        # alert that comes from webhook
        if event.get("ProblemID"):
            tags = event.get("tags", [])
            impacted_entities = event.get("ImpactedEntities", [])
            alert_dto = AlertDto(
                id=event.get("ProblemID") or event.get("problemId"),
                name=event.get("ProblemTitle") or event.get("display"),
                status=event.get("State"),
                severity=event.get("ProblemSeverity", None),
                lastReceived=datetime.datetime.now().isoformat(),
                fatigueMeter=random.randint(0, 100),
                description=event.get("ProblemTitle"),
                source=["dynatrace"],
                impact=event.get("ProblemImpact"),
                tags=tags,
                impactedEntities=impacted_entities,
                url=event.get("ProblemURL"),
            )
        # else, problem from the problem API
        else:
            alert_dto = AlertDto(
                id=event.get("problemId"),
                name=event.get("displayId"),
                status=event.get("status"),
                severity=event.get("severityLevel", None),
                lastReceived=datetime.datetime.now().isoformat(),
                fatigueMeter=random.randint(0, 100),
                description=event.get("title"),
                source=["dynatrace"],
                impact=event.get("impactLevel"),
                tags=event.get("entityTags"),
                impactedEntities=event.get("impactedEntities", []),
                url=event.get("ProblemURL"),
            )
        return alert_dto

    def _get_alerting_profiles(self):
        self.logger.info("Getting alerting profiles")
        response = requests.get(
            f"https://{self.authentication_config.environment_id}.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:alerting.profile",
            headers={
                "Authorization": f"Api-Token {self.authentication_config.api_token}"
            },
        )
        if response.ok:
            self.logger.info(f"Got alerting profiles")
            return response.json().get("items")
        elif "Use one of: settings.read" in response.text:
            self.logger.info(
                f"Failed to get alerting profiles - missing settings.read scope"
            )
            raise Exception("Token is missing required scope - settings.read (403)")
        else:
            self.logger.info(
                f"Failed to get alerting profiles - {response.status_code} {response.text}"
            )
            raise Exception(
                f"Failed to get alerting profiles: {response.status_code} {response.text}"
            )

    def setup_webhook(
        self, tenant_id: str, keep_api_url: str, api_key: str, setup_alerts: bool = True
    ):
        """
        Setup Dynatrace webhook.

        Scope needed: environment (settings.write?)
        docs: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/builtin-problem-notifications#WebHookNotification
              https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/post-object
        """
        self.logger.info("Setting up Dynatrace webhook")
        # how to get it?
        alerting_profile_id = None
        alerting_profiles = self._get_alerting_profiles()
        for alerting_profile in alerting_profiles:
            if (
                alerting_profile.get("value").get("name")
                == self.authentication_config.alerting_profile
            ):
                alerting_profile_id = alerting_profile.get("objectId")
                self.logger.info(
                    f"Found alerting profile {self.authentication_config.alerting_profile} with id {alerting_profile_id}"
                )
                break

        if not alerting_profile_id:
            self.logger.info(
                f"Cannot find alerting profile {self.authentication_config.alerting_profile} in {alerting_profiles}"
            )
            raise Exception(
                f"Cannot find alerting profile {self.authentication_config.alerting_profile}"
            )

        auth_header = f"api_key:{api_key}"
        auth_header = base64.b64encode(auth_header.encode()).decode()
        payload = {
            "enabled": True,
            "displayName": f"Keep Webhook Integration - push alerts to Keep [tenant: {tenant_id}]",
            "type": "WEBHOOK",
            "alertingProfile": alerting_profile_id,
            "webHookNotification": {
                "acceptAnyCertificate": True,
                "headers": [
                    {
                        "name": "Authorization",
                        "secret": True,
                        "secretValue": f"Basic {auth_header}",
                    }
                ],
                "url": keep_api_url,
                "notifyClosedProblems": True,
                "notifyEventMergesEnabled": True,
                # all the fields - https://docs.dynatrace.com/docs/observe-and-explore/notifications-and-alerting/problem-notifications/webhook-integration#example-json-with-placeholders
                "payload": '{\n"State":"{State}",\n"ProblemID":"{ProblemID}",\n"ProblemTitle":"{ProblemTitle}",\n"ImpactedEntities": {ImpactedEntities},\n "PID": "{PID}",\n "ProblemDetailsJSON": {ProblemDetailsJSON},\n "ProblemImpact" : "{ProblemImpact}",\n"ProblemSeverity": "{ProblemSeverity}",\n "ProblemURL": "{ProblemURL}",\n"State": "{State}",\n"Tags": "{Tags}"\n\n}',
            },
        }
        actual_payload = [
            {
                "schemaId": "builtin:problem.notifications",
                "scope": "environment",
                "value": payload,
            }
        ]
        url = f"https://{self.authentication_config.environment_id}.live.dynatrace.com/api/v2/settings/objects"
        # if its a dry run to validate the scopes
        if not setup_alerts:
            url = f"https://{self.authentication_config.environment_id}.live.dynatrace.com/api/v2/settings/objects?validateOnly=true"

        # install the webhook
        response = requests.post(
            url,
            json=actual_payload,
            headers={
                "Authorization": f"Api-Token {self.authentication_config.api_token}"
            },
        )
        if not response.ok:
            # understand if its localhost:
            violation_message = (
                response.json()[0]
                .get("error")
                .get("constraintViolations")[0]
                .get("message")
            )
            if (
                violation_message
                == "The environment does not allow for site-local URLs"
            ):
                raise Exception(
                    f"Dynatrace doesn't support use localhost as a webhook URL, use a public URL when installing dynatrace webhook."
                )
            else:
                raise Exception(
                    f"Failed to setup Dynatrace webhook: {response.status_code} {response.text}"
                )
        else:
            return True

    def dispose(self):
        """
        Dispose the provider.
        """
        pass

    def validate_config(self):
        """
        Validates required configuration for Dynatrace provider.

        """
        self.authentication_config = DynatraceProviderAuthConfig(
            **self.config.authentication
        )


if __name__ == "__main__":
    # Output debug messages
    import logging

    logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

    # Load environment variables
    import os

    api_token = os.environ.get("DYNATRACE_API_TOKEN")
    environment_id = os.environ.get("DYNATRACE_ENVIRONMENT_ID")
    from keep.api.core.dependencies import SINGLE_TENANT_UUID

    context_manager = ContextManager(tenant_id=SINGLE_TENANT_UUID)
    config = {
        "authentication": {
            "api_token": api_token,
            "environment_id": environment_id,
        }
    }
    provider = ProvidersFactory.get_provider(
        context_manager,
        provider_id="dynatrace-keephq",
        provider_type="dynatrace",
        provider_config=config,
    )
    problems = provider._get_alerts()
    provider.setup_webhook(
        tenant_id=SINGLE_TENANT_UUID,
        keep_api_url=os.environ.get("KEEP_API_URL"),
        api_key=context_manager.api_key,
        setup_alerts=True,
    )
