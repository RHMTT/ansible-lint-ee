"""Implementation of the required cron name value."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.errors import MatchError
    from ansiblelint.file_utils import Lintable
    from ansiblelint.utils import Task


class CronRequiresNameKeyParam(AnsibleLintRule):
    """Cron now requires name"""

    id = "Cron_requires_Name_Key_Param"
    shortdesc = 'Cron now requires a name key'
    description = 'Add the name key to Cron tasks.'
    severity = "HIGH"
    tags = ["cron"]
    version_added = "2.12"

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,

    ) -> list[MatchError]:
        result = []
        if (
            task["__ansible_action_type__"] in ["task", "meta"]
            and task["action"]["__ansible_module__"] == "cron"
            and (
                "name" not in task.action
            )
        ):
            result.append(self.create_matcherror(filename=file))
        return result

