"""ldap_attrs and ldap_entry module removed params key."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.errors import MatchError
    from ansiblelint.file_utils import Lintable
    from ansiblelint.utils import Task


class LdapAttrChanged(AnsibleLintRule):
    """ldap_attrs and ldap_entry no longer uses params"""

    id = "ldap_attr_has changed to ldap_attrs"
    shortdesc = 'ldap_attrs or ldap_entry deprecated params'
    description = 'Remove the params key from the ldap_attrs or ldap_entry module.'
    severity = "HIGH"
    tags = ["ldap_attr"]
    version_added = "2.9"

    _commands = [
        "ldap_attrs",
        "ldap_entry",
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
                "params" in task.action
            )
        ):
            result.append(self.create_matcherror(filename=file))
        return result
