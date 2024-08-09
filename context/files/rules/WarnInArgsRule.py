"""Implementation of the warn in args rule."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.errors import MatchError
    from ansiblelint.file_utils import Lintable
    from ansiblelint.utils import Task


class WarnInArgsRule(AnsibleLintRule):
    """Shouldnt set change with args with shell command etc."""

    id = "warn_ignore_depricated"
    shortdesc = 'Cant use warn args from command or shell'
    description = 'Remove the args, warn from the command or shell module.'
    severity = "HIGH"
    tags = ["command-shell", "idempotency"]
    version_added = "historic"

    _commands = [
        "ansible.builtin.command",
        "ansible.builtin.shell",
        "ansible.legacy.command",
        "ansible.legacy.shell",
        "command",
        "shell",
    ]

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,

    ) -> list[MatchError]:
        result = []
        if (
            task["__ansible_action_type__"] in ["task", "meta"]
            and task["action"]["__ansible_module__"] in self._commands
            and (
                "warn" in task.args
            )
        ):
            result.append(self.create_matcherror(filename=file))
        return result

