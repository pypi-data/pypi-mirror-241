"""
JiraProvider is a class that implements the BaseProvider interface for Jira updates.
"""
import dataclasses
from typing import Dict, List, Literal
from urllib.parse import urlencode, urljoin

import pydantic
import requests
from requests.auth import HTTPBasicAuth

from keep.contextmanager.contextmanager import ContextManager
from keep.exceptions.provider_exception import ProviderException
from keep.providers.base.base_provider import BaseProvider
from keep.providers.models.provider_config import ProviderConfig, ProviderScope


@pydantic.dataclasses.dataclass
class JiraProviderAuthConfig:
    """Jira authentication configuration."""

    email: str = dataclasses.field(
        metadata={
            "required": True,
            "description": "Atlassian Jira Email",
            "sensitive": False,
            "documentation_url": "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token",
        }
    )

    api_token: str = dataclasses.field(
        metadata={
            "required": True,
            "description": "Atlassian Jira API Token",
            "sensitive": True,
            "documentation_url": "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token",
        }
    )
    host: str = dataclasses.field(
        metadata={
            "required": True,
            "description": "Atlassian Jira Host",
            "sensitive": False,
            "documentation_url": "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token",
            "hint": "keephq.atlassian.net",
        }
    )


class JiraProvider(BaseProvider):
    """Enrich alerts with Jira tickets."""

    PROVIDER_SCOPES = [
        ProviderScope(
            name="BROWSE_PROJECTS",
            description="Browse Jira Projects",
            mandatory=True,
            alias="Browse projects",
        ),
        ProviderScope(
            name="CREATE_ISSUES",
            description="Create Jira Issues",
            mandatory=True,
            alias="Create issue",
        ),
        ProviderScope(
            name="CLOSE_ISSUES",
            description="Close Jira Issues",
            mandatory=False,
            alias="Close issues",
        ),
        ProviderScope(
            name="EDIT_ISSUES",
            description="Edit Jira Issues",
            mandatory=False,
            alias="Edit issues",
        ),
        ProviderScope(
            name="DELETE_ISSUES",
            description="Delete Jira Issues",
            mandatory=False,
            alias="Delete issues",
        ),
        ProviderScope(
            name="MODIFY_REPORTER",
            description="Modify Jira Issue Reporter",
            mandatory=False,
            alias="Modidy issue reporter",
        ),
    ]

    def __init__(
        self, context_manager: ContextManager, provider_id: str, config: ProviderConfig
    ):
        super().__init__(context_manager, provider_id, config)

    def validate_scopes(self):
        """
        Validate that the provider has the required scopes.
        """

        headers = {"Accept": "application/json"}
        auth = requests.auth.HTTPBasicAuth(
            self.authentication_config.email, self.authentication_config.api_token
        )

        # first, validate user/api token are correct:
        resp = requests.get(
            f"{self.jira_host}/rest/api/3/myself",
            headers={"Accept": "application/json"},
            auth=auth,
        )
        try:
            resp.raise_for_status()
        except Exception as e:
            scopes = {
                scope.name: f"Failed to authenticate with Jira - wrong credentials"
                for scope in JiraProvider.PROVIDER_SCOPES
            }
            return scopes

        params = {
            "permissions": ",".join(
                [scope.name for scope in JiraProvider.PROVIDER_SCOPES]
            )
        }
        resp = requests.get(
            f"{self.jira_host}/rest/api/3/mypermissions",
            headers=headers,
            auth=auth,
            params=params,
        )
        try:
            resp.raise_for_status()
        except Exception as e:
            scopes = {scope.name: f"Failed to authenticate with Jira: {e}"}
            return scopes
        permissions = resp.json().get("permissions", [])
        scopes = {
            scope: scope_result.get("havePermission", False)
            for scope, scope_result in permissions.items()
        }
        return scopes

    def validate_config(self):
        self.authentication_config = JiraProviderAuthConfig(
            **self.config.authentication
        )

    @property
    def jira_host(self):
        host = (
            self.authentication_config.host
            if self.authentication_config.host.startswith("https://")
            else f"https://{self.authentication_config.host}"
        )
        return host

    def dispose(self):
        """
        No need to dispose of anything, so just do nothing.
        """
        pass

    def __get_url(self, paths: List[str] = [], query_params: dict = None, **kwargs):
        """
        Helper method to build the url for jira api requests.

        Example:

        paths = ["issue", "createmeta"]
        query_params = {"projectKeys": "key1"}
        url = __get_url("test", paths, query_params)

        # url = https://test.atlassian.net/rest/api/2/issue/createmeta?projectKeys=key1
        """
        # add url path

        url = urljoin(
            f"{self.jira_host}/rest/api/2/",
            "/".join(str(path) for path in paths),
        )

        # add query params
        if query_params:
            url = f"{url}?{urlencode(query_params)}"

        return url

    def __get_auth(self):
        """
        Helper method to build the auth payload for jira api requests.
        """
        return HTTPBasicAuth(
            self.authentication_config.email, self.authentication_config.api_token
        )

    def __get_createmeta(self, project_key: str):
        try:
            self.logger.info("Fetching create meta data...")

            url = self.__get_url(
                paths=["issue", "createmeta"],
                query_params={"projectKeys": project_key},
            )

            response = requests.get(url=url, auth=self.__get_auth())

            response.raise_for_status()

            self.logger.info("Fetched create meta data!")

            return response.json()
        except Exception as e:
            raise ProviderException(f"Failed to fetch createmeta: {e}")

    def __get_single_createmeta(self, project_key: str):
        """
        Helper method to get single createmeta. As the original createmeta api returns
        multiple issue types and other config.
        """
        try:
            self.logger.info("Fetching single createmeta...")

            createmeta = self.__get_createmeta(project_key)

            projects = createmeta.get("projects", [])
            project = projects[0] if len(project_key) > 0 else {}

            issuetypes = project.get("issuetypes", [])
            issuetype = issuetypes[0] if len(issuetypes) > 0 else {}

            issue_type_name = issuetype.get("name", "")
            if not issue_type_name:
                raise ProviderException("No issue types found!")

            self.logger.info("Fetched single createmeta!")

            return {"issue_type_name": issue_type_name}
        except Exception as e:
            raise ProviderException(f"Failed to fetch single createmeta: {e}")

    def __create_issue(
        self,
        project_key: str,
        summary: str,
        description: str = "",
        issue_type: str = "",
        **kwargs: dict,
    ):
        """
        Helper method to create an issue in jira.
        """
        try:
            self.logger.info("Creating an issue...")

            if not issue_type:
                create_meta = self.__get_single_createmeta(project_key=project_key)
                issue_type = create_meta.get("issue_type_name", "")

            url = self.__get_url(paths=["issue"])

            request_body = {
                "fields": {
                    "summary": summary,
                    "description": description,
                    "project": {"key": project_key},
                    "issuetype": {"name": issue_type},
                }
            }

            response = requests.post(url=url, json=request_body, auth=self.__get_auth())
            try:
                response.raise_for_status()
            except Exception as e:
                self.logger.exception(
                    "Failed to create an issue", extra=response.json()
                )
                raise ProviderException(f"Failed to create an issue: {response.json()}")
            self.logger.info("Created an issue!")

            return {"issue": response.json()}
        except Exception as e:
            raise ProviderException(f"Failed to create an issue: {e}")

    def _extract_project_key_from_board_name(self, board_name: str):
        boards_response = requests.get(
            f"{self.jira_host}/rest/agile/1.0/board",
            auth=self.__get_auth(),
            headers={"Accept": "application/json"},
        )
        if boards_response.status_code == 200:
            for board in boards_response.json()["values"]:
                if board["name"].lower() == board_name.lower():
                    return board["location"]["projectKey"]
        else:
            raise Exception("Could not fetch boards: " + boards_response.text)

    def _notify(
        self,
        **kwargs: dict,
    ):
        """
        Notify jira by creating an issue.
        """
        # extracrt the required params
        project_key = kwargs.get("project_key", "")
        board_name = kwargs.get("board_name", "")
        if board_name:
            project_key = self._extract_project_key_from_board_name(board_name)
        summary = kwargs.get("summary", "")
        description = kwargs.get("description", "")
        issue_type = kwargs.get("issuetype", "")
        if not project_key or not summary or not issue_type or not description:
            raise ProviderException("Project key and summary are required!")
        try:
            self.logger.info("Notifying jira...")
            result = self.__create_issue(
                project_key=project_key,
                summary=summary,
                description=description,
                issue_type=issue_type,
            )
            result["ticket_url"] = f"{self.jira_host}/browse/{result['issue']['key']}"
            self.logger.info("Notified jira!")

            return result
        except Exception as e:
            context = {
                "summary": summary,
                "description": description,
                "issue_type": issue_type,
                "project_key": project_key,
            }
            raise ProviderException(f"Failed to notify jira: {e} - Params: {context}")

    def _query(self, board_id="", **kwargs: dict):
        """
        API for fetching issues:
        https://developer.atlassian.com/cloud/jira/software/rest/api-group-board/#api-rest-agile-1-0-board-boardid-issue-get

        Args:
            kwargs (dict): The providers with context
        """
        self.logger.debug("Fetching data from Jira")

        jira_api_token = self.authentication_config.api_token

        request_url = f"https://{self.jira_host}/rest/agile/1.0/board/{board_id}/issue"
        response = requests.get(request_url, auth=self.__get_auth())
        if not response.ok:
            raise ProviderException(
                f"{self.__class__.__name__} failed to fetch data from Jira: {response.text}"
            )
        self.logger.debug("Fetched data from Jira")

        issues = response.json()
        return {"number_of_issues": issues["total"]}


if __name__ == "__main__":
    # Output debug messages
    import logging

    logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
    context_manager = ContextManager(
        tenant_id="singletenant",
        workflow_id="test",
    )
    # Load environment variables
    import os

    jira_api_token = os.environ.get("JIRA_API_TOKEN")
    jira_email = os.environ.get("JIRA_EMAIL")
    jira_host = os.environ.get("JIRA_HOST")

    # Initalize the provider and provider config
    config = ProviderConfig(
        description="Jira Input Provider",
        authentication={
            "api_token": jira_api_token,
            "email": jira_email,
            "host": jira_host,
        },
    )
    provider = JiraProvider(context_manager, provider_id="jira", config=config)
    scopes = provider.validate_scopes()
    # Create ticket
    provider.notify(
        board_name="Oncall Board",
        issue_type="Bug",
        summary="Test",
        description="Test",
    )
