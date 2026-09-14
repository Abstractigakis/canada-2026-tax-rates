"""Published 2026 Canadian tax and payroll figures. Not tax advice."""

from __future__ import annotations

import json
from pathlib import Path

_JSON = Path(__file__).resolve().parent / "rates-2026.json"


def load() -> dict:
    return json.loads(_JSON.read_text(encoding="utf-8"))


RATES = load()
YEAR = RATES["year"]
CURRENCY = RATES["currency"]
