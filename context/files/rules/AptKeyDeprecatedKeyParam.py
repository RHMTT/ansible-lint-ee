"""Implementation of the deprecated key removed from apt_key."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.errors import MatchError
    from ansiblelint.file_utils import Lintable
    from ansiblelint.utils import Task


class AptKeyDeprecatedKeyParam(AnsibleLintRule):
    """Key param has been deprecated from apt_key module"""

    id = "Apt_Key_Deprecated_Key_Param"
    shortdesc = 'Cant use key with apt_ket'
    description = 'Remove the key attribute to the apt_key module.'
    severity = "HIGH"
    tags = ["apt_key", "security"]
    version_added = "2.10"

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,

    ) -> list[MatchError]:
        result = []
        if (
            task["__ansible_action_type__"] in ["task", "meta"]
            and task["action"]["__ansible_module__"] == "apt_key"
            and (
                "key" in task.action
            )
        ):
            result.append(self.create_matcherror(filename=file))
        return result

