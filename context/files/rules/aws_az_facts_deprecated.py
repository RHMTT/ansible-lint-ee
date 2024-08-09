"""Implementation of the deprecated aws_az_facts module."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.errors import MatchError
    from ansiblelint.file_utils import Lintable
    from ansiblelint.utils import Task


class AwsAzFactsDeprecated(AnsibleLintRule):
    """aws_az_facts module has been changed to aws_az_info"""

    id = "aws_az_facts_deprecated"
    shortdesc = 'aws_az_facts is deprecated'
    description = 'Change aws_az_facts to aws_az_info'
    severity = "HIGH"
    tags = ["aws_az_facts", "module_change"]
    version_added = "2.9"

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,

    ) -> list[MatchError]:
        result = []
        if (
            task["__ansible_action_type__"] in ["task", "meta"]
            and task["action"]["__ansible_module__"] == "aws_az_facts"
        ):
            result.append(self.create_matcherror(filename=file))
        return result

