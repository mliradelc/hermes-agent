"""Regression tests for scripts/contributor_audit.py ignore rules."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_contributor_audit_module():
    spec = importlib.util.spec_from_file_location(
        "_contributor_audit_under_test",
        Path(__file__).resolve().parents[2] / "scripts" / "contributor_audit.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_is_ignored_skips_local_hermes_agent_email():
    module = _load_contributor_audit_module()

    assert module.is_ignored("Hermes Agent", "hermes-agent@local")


def test_is_ignored_does_not_skip_normal_human_email():
    module = _load_contributor_audit_module()

    assert not module.is_ignored("mliradelc", "person@example.com")
