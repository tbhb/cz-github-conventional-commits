from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from commitizen import git
from commitizen.config import BaseConfig
from commitizen.cz.base import BaseCommitizen
from commitizen.question import CzQuestion
from jinja2 import PackageLoader


class GitHubConventionalCz(BaseCommitizen):
    template_loader = PackageLoader("cz_github_conventional", "templates")

    def __init__(self, config: BaseConfig) -> None:
        super().__init__(config)

    def questions(self) -> list[CzQuestion]:
        return []

    def message(self, answers: Mapping[str, Any]) -> str:
        return ""

    def example(self) -> str:
        return ""

    def schema(self) -> str:
        return ""

    def schema_pattern(self) -> str:
        return ""

    def info(self) -> str:
        return ""

    def changelog_hook(self, full_changelog: str, partial_changelog: str | None) -> str:
        return full_changelog

    def changelog_message_builder_hook(
        self, parsed_message: dict[str, Any], commit: git.GitCommit
    ) -> dict[str, Any]:
        return parsed_message

    def changelog_release_hook(
        self, release: dict[str, Any], tag: git.GitTag | None
    ) -> dict[str, Any]:
        return release
