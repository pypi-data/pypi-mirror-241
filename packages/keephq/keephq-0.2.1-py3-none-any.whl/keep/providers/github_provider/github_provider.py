"""
GithubProvider is a provider that interacts with GitHub.
"""

import dataclasses

import pydantic
from github import Github

from keep.contextmanager.contextmanager import ContextManager
from keep.providers.base.base_provider import BaseProvider
from keep.providers.models.provider_config import ProviderConfig


@pydantic.dataclasses.dataclass
class GithubProviderAuthConfig:
    """
    GithubProviderAuthConfig is a class that represents the authentication configuration for the GithubProvider.
    """

    access_token: str | None = dataclasses.field(
        metadata={
            "required": True,
            "description": "GitHub Access Token",
            "sensitive": True,
        }
    )


class GithubProvider(BaseProvider):
    """
    Enrich alerts with data from GitHub.
    """

    def __init__(
        self, context_manager: ContextManager, provider_id: str, config: ProviderConfig
    ):
        super().__init__(context_manager, provider_id, config)
        self.client = self.__generate_client()

    def __generate_client(self):
        # Should get an access token once we have a real use case for GitHub provider
        if self.authentication_config.access_token:
            client = Github(self.authentication_config.access_token)
        else:
            client = Github()
        return client

    def dispose(self):
        """
        Dispose of the provider.
        """
        pass

    def validate_config(self):
        self.authentication_config = GithubProviderAuthConfig(
            **self.config.authentication
        )


class GithubStarsProvider(GithubProvider):
    """
    GithubStarsProvider is a class that provides a way to read stars from a GitHub repository.
    """

    def __init__(
        self, context_manager: ContextManager, provider_id: str, config: ProviderConfig
    ):
        super().__init__(context_manager, provider_id, config)

    def _query(
        self, repository: str, previous_stars_count: int = 0, **kwargs: dict
    ) -> dict:
        repo = self.client.get_repo(repository)
        stars_count = repo.stargazers_count
        new_stargazers = []

        if not previous_stars_count:
            previous_stars_count = 0

        self.logger.debug(f"Previous stargazers: {previous_stars_count}")
        self.logger.debug(f"New stargazers: {stars_count - int(previous_stars_count)}")
        if previous_stars_count and int(previous_stars_count) > 0:
            stargazers_with_dates = list(repo.get_stargazers_with_dates())[
                int(previous_stars_count) :
            ]
            for stargazer in stargazers_with_dates:
                new_stargazers.append(
                    {
                        "username": stargazer.user.login,
                        "starred_at": str(stargazer.starred_at),
                    }
                )
                self.logger.debug(f"New stargazer: {stargazer.user.login}")
        return {
            "stars": stars_count,
            "new_stargazers": new_stargazers,
            "new_stargazers_count": len(new_stargazers),
        }


if __name__ == "__main__":
    import os

    context_manager = ContextManager(
        tenant_id="singletenant",
        workflow_id="test",
    )
    github_stars_provider = GithubStarsProvider(
        context_manager,
        "test",
        ProviderConfig(authentication={"access_token": os.environ.get("GITHUB_PAT")}),
    )

    result = github_stars_provider.query(
        repository="keephq/keep", previous_stars_count=910
    )
    print(result)
