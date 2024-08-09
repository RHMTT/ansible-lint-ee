"""Implementation of the deprecated key recmoved from apt_key."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.errors import MatchError
    from ansiblelint.file_utils import Lintable
    from ansiblelint.utils import Task


class geturlDeprecatedsha256Param(AnsibleLintRule):
    """sha256 param has been deprecated from get_url module"""

    id = "get_url_Deprecated_sha256_Param"
    severity = "HIGH"
    shortdesc = 'Cant use sha256 param with get_url module'
    description = 'Remove the sha256 param from the get_url module.'
    tags = ["get_url", "security"]
    version_added = "2.14"

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,

    ) -> list[MatchError]:
        result = []
        if (
            task["__ansible_action_type__"] in ["task", "meta"]
            and task["action"]["__ansible_module__"] == "get_url"
            and (
                "sha256" in task.action
            )
        ):
            result.append(self.create_matcherror(filename=file))
        return result

