import io
import json
import logging
import os
import typing

import requests
import yaml

from keep.api.core.db import get_workflow_id
from keep.contextmanager.contextmanager import ContextManager
from keep.iohandler.iohandler import IOHandler
from keep.providers.base.base_provider import BaseProvider
from keep.providers.providers_factory import ProvidersFactory
from keep.step.step import Step, StepType
from keep.workflowmanager.workflow import Workflow


class Parser:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def _get_workflow_id(self, tenant_id, workflow: dict) -> str:
        """Support both CLI and API workflows

        Args:
            workflow (dict): _description_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """
        # for backward compatibility reasons, the id on the YAML is actually the name
        # and the id is a unique generated id stored in the db
        workflow_name = workflow.get("id")
        if workflow_name is None:
            raise ValueError("Workflow dict must have an id")

        # get the workflow id from the database
        workflow_id = get_workflow_id(tenant_id, workflow_name)
        # if the workflow id is not found, it means that the workflow is not stored in the db
        # for example when running from CLI
        # so for backward compatibility, we will use the workflow name as the id
        # todo - refactor CLI to use db also
        if not workflow_id:
            workflow_id = workflow_name
        return workflow_id

    def parse(
        self, tenant_id, parsed_workflow_yaml: dict, providers_file: str = None
    ) -> typing.List[Workflow]:
        """_summary_

        Args:
            parsed_workflow_yaml (str): could be a url or a file path
            providers_file (str, optional): _description_. Defaults to None.

        Returns:
            typing.List[Workflow]: _description_
        """
        # Parse the workflow itself (the alerts here is backward compatibility)
        workflow_providers = parsed_workflow_yaml.get("providers")
        if parsed_workflow_yaml.get("workflows") or parsed_workflow_yaml.get("alerts"):
            raw_workflows = parsed_workflow_yaml.get(
                "workflows"
            ) or parsed_workflow_yaml.get("alerts")
            workflows = [
                self._parse_workflow(
                    tenant_id, workflow, providers_file, workflow_providers
                )
                for workflow in raw_workflows
            ]
        # the alert here is backward compatibility
        elif parsed_workflow_yaml.get("workflow") or parsed_workflow_yaml.get("alert"):
            raw_workflow = parsed_workflow_yaml.get(
                "workflow"
            ) or parsed_workflow_yaml.get("alert")
            workflow = self._parse_workflow(
                tenant_id, raw_workflow, providers_file, workflow_providers
            )
            workflows = [workflow]
        # else, if it stored in the db, it stored without the "workflow" key
        else:
            workflow = self._parse_workflow(
                tenant_id, parsed_workflow_yaml, providers_file, workflow_providers
            )
            workflows = [workflow]
        return workflows

    def _get_workflow_provider_types_from_steps_and_actions(
        self, steps: list[Step], actions: list[Step]
    ) -> list[str]:
        provider_types = []
        steps_and_actions = [*steps, *actions]
        for step_or_action in steps_and_actions:
            try:
                provider_type = step_or_action.provider.provider_type
                if provider_type not in provider_types:
                    provider_types.append(provider_type)
            except:
                self.logger.warn(
                    "Could not get provider type from step or action",
                    extra={"step_or_action": step_or_action},
                )
        return provider_types

    def _parse_workflow(
        self,
        tenant_id,
        workflow: dict,
        providers_file: str,
        workflow_providers: dict = None,
    ) -> Workflow:
        self.logger.debug("Parsing workflow")
        workflow_id = self._get_workflow_id(tenant_id, workflow)
        context_manager = ContextManager(
            tenant_id=tenant_id,
            workflow_id=workflow_id,
        )
        # Parse the providers (from the workflow yaml or from the providers directory)
        self._load_providers_config(
            tenant_id, context_manager, workflow, providers_file, workflow_providers
        )
        workflow_id = self._parse_id(workflow)
        workflow_owners = self._parse_owners(workflow)
        workflow_tags = self._parse_tags(workflow)
        workflow_steps = self._parse_steps(context_manager, workflow)
        workflow_actions = self._parse_actions(context_manager, workflow)
        workflow_interval = self.parse_interval(workflow)
        on_failure_action = self._get_on_failure_action(workflow)
        workflow_triggers = self.get_triggers_from_workflow(workflow)
        workflow_provider_types = (
            self._get_workflow_provider_types_from_steps_and_actions(
                workflow_steps, workflow_actions
            )
        )
        workflow = Workflow(
            workflow_id=workflow_id,
            workflow_description=workflow.get("description"),
            workflow_owners=workflow_owners,
            workflow_tags=workflow_tags,
            workflow_interval=workflow_interval,
            workflow_triggers=workflow_triggers,
            workflow_steps=workflow_steps,
            workflow_actions=workflow_actions,
            on_failure=on_failure_action,
            context_manager=context_manager,
            workflow_providers_type=workflow_provider_types,
        )
        self.logger.debug("Workflow parsed successfully")
        return workflow

    def _load_providers_config(
        self,
        tenant_id,
        context_manager: ContextManager,
        workflow: dict,
        providers_file: str,
        workflow_providers: dict = None,
    ):
        self.logger.debug("Parsing providers")
        providers_file = (
            providers_file or os.environ.get("KEEP_PROVIDERS_FILE") or "providers.yaml"
        )
        if providers_file and os.path.exists(providers_file):
            self._parse_providers_from_file(context_manager, providers_file)

        # if the workflow file itself contain providers (mainly backward compatibility)
        if workflow_providers:
            context_manager.providers_context.update(workflow_providers)

        self._parse_providers_from_env(context_manager)
        self._load_providers_from_db(context_manager, tenant_id)
        self.logger.debug("Providers parsed and loaded successfully")

    def _load_providers_from_db(
        self, context_manager: ContextManager, tenant_id: str = None
    ):
        """_summary_

        Args:
            context_manager (ContextManager): _description_
            tenant_id (str, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        # If there is no tenant id, e.g. running from CLI, no db here
        if not tenant_id:
            return
        # Load installed providers
        all_providers = ProvidersFactory.get_all_providers()
        installed_providers = ProvidersFactory.get_installed_providers(
            tenant_id=tenant_id, all_providers=all_providers
        )
        for provider in installed_providers:
            self.logger.debug(f"Loading provider", extra={"provider_id": provider.id})
            try:
                provider_name = provider.details.get("name")
                context_manager.providers_context[provider.id] = provider.details
                # map also the name of the provider, not only the id
                # so that we can use the name to reference the provider
                context_manager.providers_context[provider_name] = provider.details
                self.logger.info(f"Provider {provider.id} loaded successfully")
            except Exception as e:
                self.logger.error(
                    f"Error loading provider {provider.id}", extra={"exception": e}
                )
        return installed_providers

    def _parse_providers_from_env(self, context_manager: ContextManager):
        """
        Parse providers from the KEEP_PROVIDERS environment variables.
            Either KEEP_PROVIDERS to load multiple providers or KEEP_PROVIDER_<provider_name> can be used.

        KEEP_PROVIDERS is a JSON string of the providers config.
            (e.g. {"slack-prod": {"authentication": {"webhook_url": "https://hooks.slack.com/services/..."}}})
        """
        providers_json = os.environ.get("KEEP_PROVIDERS")
        if providers_json:
            try:
                self.logger.debug(
                    "Parsing providers from KEEP_PROVIDERS environment variable"
                )
                context_manager.providers_context.update(json.loads(providers_json))
                self.logger.debug(
                    "Providers parsed successfully from KEEP_PROVIDERS environment variable"
                )
            except json.JSONDecodeError:
                self.logger.error(
                    "Error parsing providers from KEEP_PROVIDERS environment variable"
                )

        for env in os.environ.keys():
            if env.startswith("KEEP_PROVIDER_"):
                # KEEP_PROVIDER_SLACK_PROD
                provider_name = (
                    env.replace("KEEP_PROVIDER_", "").replace("_", "-").lower()
                )
                try:
                    self.logger.debug(f"Parsing provider {provider_name} from {env}")
                    # {'authentication': {'webhook_url': 'https://hooks.slack.com/services/...'}}
                    provider_config = json.loads(os.environ.get(env))
                    context_manager.providers_context[provider_name] = provider_config
                    self.logger.debug(
                        f"Provider {provider_name} parsed successfully from {env}"
                    )
                except json.JSONDecodeError:
                    self.logger.error(
                        f"Error parsing provider config from environment variable {env}"
                    )

    def _parse_providers_from_workflow(
        self, context_manager: ContextManager, workflow: dict
    ) -> typing.List[BaseProvider]:
        context_manager.providers_context.update(workflow.get("providers"))
        self.logger.debug("Workflow providers parsed successfully")

    def _parse_providers_from_file(
        self, context_manager: ContextManager, providers_file: str
    ):
        with open(providers_file, "r") as file:
            try:
                providers = yaml.safe_load(file)
            except yaml.YAMLError:
                self.logger.exception(f"Error parsing providers file {providers_file}")
                raise
            context_manager.providers_context.update(providers)
        self.logger.debug("Providers config parsed successfully")

    def _parse_id(self, workflow) -> str:
        workflow_id = workflow.get("id")
        if workflow_id is None:
            raise ValueError("Workflow ID is required")
        return workflow_id

    def _parse_owners(self, workflow) -> typing.List[str]:
        workflow_owners = workflow.get("owners", [])
        return workflow_owners

    def _parse_tags(self, workflow) -> typing.List[str]:
        workflow_tags = workflow.get("tags", [])
        return workflow_tags

    def parse_interval(self, workflow) -> int:
        # backward compatibility
        workflow_interval = workflow.get("interval", 0)
        triggers = workflow.get("triggers", [])
        for trigger in triggers:
            if trigger.get("type") == "interval":
                workflow_interval = trigger.get("value", 0)
        return workflow_interval

    def _parse_steps(
        self, context_manager: ContextManager, workflow
    ) -> typing.List[Step]:
        self.logger.debug("Parsing steps")
        workflow_steps = workflow.get("steps", [])
        workflow_steps_parsed = []
        for _step in workflow_steps:
            provider = self._get_step_provider(context_manager, _step)
            provider_parameters = _step.get("provider", {}).get("with")
            step_id = _step.get("name")
            step = Step(
                context_manager=context_manager,
                step_id=step_id,
                config=_step,
                provider=provider,
                provider_parameters=provider_parameters,
                step_type=StepType.STEP,
            )
            workflow_steps_parsed.append(step)
        self.logger.debug("Steps parsed successfully")
        return workflow_steps_parsed

    def _get_step_provider(self, context_manager: ContextManager, _step: dict) -> dict:
        step_provider = _step.get("provider")
        try:
            step_provider_type = step_provider.pop("type")
        except AttributeError:
            raise ValueError("Step provider type is required")
        try:
            step_provider_config = step_provider.pop("config")
        except KeyError:
            step_provider_config = {"authentication": {}}
        provider_id, provider_config = self._parse_provider_config(
            context_manager, step_provider_type, step_provider_config
        )
        provider = ProvidersFactory.get_provider(
            context_manager, provider_id, step_provider_type, provider_config
        )
        return provider

    def _get_action(
        self,
        context_manager: ContextManager,
        action: dict,
        action_name: str | None = None,
    ) -> Step:
        name = action_name or action.get("name")
        provider_config = action.get("provider").get("config")
        provider_parameters = action.get("provider").get("with", {})
        provider_type = action.get("provider").get("type")
        provider_id, provider_config = self._parse_provider_config(
            context_manager, provider_type, provider_config
        )
        provider = ProvidersFactory.get_provider(
            context_manager,
            provider_id,
            provider_type,
            provider_config,
            **provider_parameters,
        )
        action = Step(
            context_manager=context_manager,
            step_id=name,
            provider=provider,
            config=action,
            provider_parameters=provider_parameters,
            step_type=StepType.ACTION,
        )
        return action

    def _parse_actions(
        self, context_manager: ContextManager, workflow
    ) -> typing.List[Step]:
        self.logger.debug("Parsing actions")
        workflow_actions = workflow.get("actions", [])
        workflow_actions_parsed = []
        for _action in workflow_actions:
            parsed_action = self._get_action(context_manager, _action)
            workflow_actions_parsed.append(parsed_action)
        self.logger.debug("Actions parsed successfully")
        return workflow_actions_parsed

    def _get_on_failure_action(self, workflow) -> Step | None:
        """
        Parse the on-failure action

        Args:
            workflow (_type_): _description_

        Returns:
            Action | None: _description_
        """
        self.logger.debug("Parsing on-faliure")
        workflow_on_failure = workflow.get("on-failure", {})
        if workflow_on_failure:
            parsed_action = self._get_action(workflow_on_failure, "on-faliure")
            self.logger.debug("Parsed on-failure successfully")
            return parsed_action
        self.logger.debug("No on-failure action")

    def _extract_provider_id(self, provider_type: str):
        """
        Translate {{ <provider_id>.<config_id> }} to a provider id

        Args:
            provider_type (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        # TODO FIX THIS SHIT
        provider_type = provider_type.split(".")
        if len(provider_type) != 2:
            raise ValueError(
                "Provider config is not valid, should be in the format: {{ <provider_id>.<config_id> }}"
            )

        provider_id = provider_type[1].replace("}}", "").strip()
        return provider_id

    def _parse_provider_config(
        self,
        context_manager: ContextManager,
        provider_type: str,
        provider_config: str | dict | None,
    ) -> tuple:
        """
        Parse provider config.
            If the provider config is a dict, return it as is.
            If the provider config is None, return an empty dict.
            If the provider config is a string, extract the config from the providers context.
            * When provider config is either dict or None, provider config id is the same as the provider type.

        Args:
            provider_type (str): The provider type
            provider_config (str | dict | None): The provider config

        Raises:
            ValueError: When the provider config is a string and the provider config id is not found in the providers context.

        Returns:
            tuple: provider id and provider parsed config
        """
        # Support providers without config such as logfile or mock
        if isinstance(provider_config, dict):
            return provider_type, provider_config
        elif provider_config is None:
            return provider_type, {"authentication": {}}
        # extract config when using {{ <provider_id>.<config_id> }}
        elif isinstance(provider_config, str):
            config_id = self._extract_provider_id(provider_config)
            provider_config = context_manager.providers_context.get(config_id)
            if not provider_config:
                self.logger.warning(
                    f"Provider {config_id} not found in configuration, did you configure it?"
                )
                provider_config = {"authentication": {}}
            return config_id, provider_config

    def get_providers_from_workflow(self, workflow: dict):
        """extract the provider names from a worklow

        Args:
            workflow (dict): _description_
        """
        actions_providers = [
            action.get("provider") for action in workflow.get("actions", [])
        ]
        steps_providers = [step.get("provider") for step in workflow.get("steps", [])]
        providers = actions_providers + steps_providers
        try:
            providers = [
                {
                    "name": p.get("config", f"NAME.{p.get('type')}")
                    .split(".")[1]
                    .replace("}}", "")
                    .strip(),
                    "type": p.get("type"),
                }
                for p in providers
            ]
        except:
            self.logger.error(
                "Failed to extract providers from workflow",
                extra={"workflow": workflow},
            )
            raise
        return providers

    def get_triggers_from_workflow(self, workflow: dict):
        """extract the trigger names from a worklow

        Args:
            workflow (dict): _description_
        """
        # triggers:
        # - type: alert
        # filters:
        # - key: alert.source
        #   value: awscloudwatch
        triggers = workflow.get("triggers", [])
        return triggers
