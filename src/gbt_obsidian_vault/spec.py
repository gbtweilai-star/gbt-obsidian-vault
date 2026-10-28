"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "obsidian_vault",
 "domain": "mind",
 "desc": "Obsidian 永久记忆层（主人令 2026-09-27「让触手的吞天拥有永久记忆 Obsidian，所有触手每一根都绑定独立的 Obsidian，再把所有的 Obsidian 和本体的自研 Obsidian 双向绑定到一起互通共享」）：**227 根触手各一本独立库**（`vaults/<触手>/`：README MOC + 记忆.md + `.obsidian/app.json`，Obsidian 直接能开）· **本体的自研库**=brain_vault 认的那本（Documents\\Codex\\ObsidianVault）· 双向 = 触手页链回 [[GBT本体记忆]] + 本体 [[触手总索引]] 链到每一本（两条都查）。**只追加、无删除路径**；不写主人自己的库（只指向）。写主人 Documents 目录时走 filesystem_write 门（`root=documents`）。op=status/provision/remember/sync_page/bind/recall/verify/where",
 "handler": "obsidian_vault",
 "safe": true,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "status",
  "provision",
  "remember",
  "sync_page",
  "bind",
  "recall",
  "verify",
  "where"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
