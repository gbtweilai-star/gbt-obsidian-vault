#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_obsidian_vault info
PYTHONPATH=src python -m gbt_obsidian_vault check --payload '{}'
PYTHONPATH=src python -m gbt_obsidian_vault run   --payload '{}'
