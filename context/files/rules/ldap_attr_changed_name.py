"""ldap_attr module has changed to ldap_attrs."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.errors import MatchError
    from ansiblelint.file_utils import Lintable
    from ansiblelint.utils import Task


class LdapAttrChanged(AnsibleLintRule):
    """ldap_attr is now ldap_attrs"""

    id = "ldap_attr_has changed to ldap_attrs"
    shortdesc = 'ldap_attr module has changed to ldap_attrs'
    description = 'Change the ldap_attr module to ldap_attrs.'
    severity = "HIGH"
    tags = ["ldap_attr"]
    version_added = "2.9"

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,

    ) -> list[MatchError]:
        result = []
        if (
            task["__ansible_action_type__"] in ["task", "meta"]
            and task["action"]["__ansible_module__"] == "ldap_attr"
        ):
            result.append(self.create_matcherror(filename=file))
        return result

