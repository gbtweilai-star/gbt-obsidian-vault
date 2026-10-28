# obsidian_vault

**One capability bit from GBT V8, packaged standalone.** No. 168 of 341,
`mind` domain (Mind).

<p>
<img alt="python" src="https://img.shields.io/badge/python-3.9%2B-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="deps" src="https://img.shields.io/badge/runtime%20dependencies-0-brightgreen">
</p>

> Obsidian 永久记忆层（主人令 2026-09-27「让触手的吞天拥有永久记忆 Obsidian，所有触手每一根都绑定独立的 Obsidian，再把所有的 Obsidian 和本体的自研 Obsidian 双向绑定到一起互通共享」）：**227 根触手各一本独立库**（`vaults/<触手>/`：README MOC + 记忆.md + `.obsidian/app.json`，Obsidian 直接能开）· **本体的自研库**=brain_vault 认的那本（Documents\Codex\ObsidianVault）· 双向 = 触手页链回 [[GBT本体记忆]] + 本体 [[触手总索引]] 链到每一本（两条都查）。**只追加、无删除路径**；不写主人自己的库（只指向）。写主人 Documents 目录时走 filesystem_write 门（`root=documents`）。op=status/provision/remember/sync_page/bind/recall/verify/where

That description is copied verbatim from the registry. `tests/test_spec.py` pins it,
so documentation drift fails the build instead of shipping quietly.

## What this package actually is

It is the **contract** for one capability: its name, its parameters, the values it
accepts, and whether it can change state that cannot be restored. It is not the
implementation — that lives in the runtime this bit was extracted from.

So `run()` goes through a narrow `Backend` protocol, and the default backend is a
stub that **says so**:

```
status="validated"   backend="stub"   data={"executed": false}
```

Never `status="ok"`. A stub that reports success is worse than no stub, because the
caller stops looking for the real thing.

## Install

```bash
git clone https://github.com/gbtweilai-star/gbt-obsidian-vault.git
cd gbt-obsidian-vault
python -m pip install -e ".[dev]"
```

## Use

```bash
python -m gbt_obsidian_vault info                  # capability card
python -m gbt_obsidian_vault spec --json           # machine-readable contract
python -m gbt_obsidian_vault check --payload '{}'
python -m gbt_obsidian_vault run   --payload '{}'
```

Real `info` output from this machine:

```text
obsidian_vault  (mind)  v1.0.0
----------------------------------------
Obsidian 永久记忆层（主人令 2026-09-27「让触手的吞天拥有永久记忆 Obsidian，所有触手每一根都绑定独立的 Obsidian，再把所有的 Obsidian 和本体的自研 Obsidian 双向绑定到一起互通共享」）：**227 根触手各一本独立库**（`vaults/<触手>/`：README MOC + 记忆.md + `.obsidian/app.json`，Obsidian 直接能开）· **本体的自研库**=brain_vault 认的那本（Documents\Codex\ObsidianVault）· 双向 = 触手页链回 [[GBT本体记忆]] + 本体 [[触手总索引]] 链到每一本（两条都查）。**只追加、无删除路径**；不写主人自己的库（只指向）。写主人 Documents 目录时走 filesystem_write 门（`root=documents`）。op=status/provision/remember/sync_page/bind/recall/verify/where

gated      : False
external   : False
multi-op   : True
params     : (none)
values     : status, provision, remember, sync_page, bind, recall, verify, where
```

Wire a real implementation:

```python
from gbt_obsidian_vault import run

class MyBackend:
    name = "my-backend"
    def invoke(self, cap, payload):
        return {"cap": cap, "handled": sorted(payload)}

result = run({}, backend=MyBackend())
assert result.status == "ok"
```

## Parameters

| name | required | notes |
|---|---|---|
| — | no | the registry declares no required parameters |

Registry hint (`params_hint`): (empty)

**注册表登记的取值 / 子动作（8 个）**：`status`、`provision`、`remember`、`sync_page`、`bind`、`recall`、`verify`、`where`

Types are deliberately absent: the registry does not declare them, and an invented
type is worse than no type, because callers believe it.

## Boundaries

- Not gated: the registry marks this bit `safe: true`.
- No external service dependency declared.
- Multi-op (`multi_op: true`): several sub-actions share one name — read `op` before calling.
- No implementation ships here. Bring a backend; the protocol is one method.

## What this is not

Not a wrapper around a hosted API. Not a model. Not a promise that calling it does
anything on its own. It is the typed seam plus the validation, which is the part that
stays correct even when the implementation changes.

## Tests

```bash
python -m pytest
```

```text
20 passed, 3 skipped in 0.11s
```

## Provenance

| field | value |
|---|---|
| capability | `obsidian_vault` |
| domain | `mind` |
| handler | `obsidian_vault` |
| safe | `True` (gated = `False`) |
| external | `False` |
| atlas page | [mind/obsidian_vault](https://github.com/gbtweilai-star/gbt-caps/blob/main/caps/mind/obsidian_vault.md) |
| full index | [https://github.com/gbtweilai-star/gbt-caps](https://github.com/gbtweilai-star/gbt-caps) |

The parent README says 348 capabilities; an AST pass over the registry enumerates
`341 + 0 unimplemented + 0 disabled = 341`. The extra 7 are historical duplicates.
Numbering here follows 341 and matches the `gbt-caps` index one-to-one.

## License

MIT.
