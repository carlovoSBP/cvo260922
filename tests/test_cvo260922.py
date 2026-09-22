"""Smoke tests for cvo260922."""

from cvo260922 import hello


def test_sanity() -> None:
    """Sanity check."""
    assert True


def test_integration() -> None:
    """Integration test for hello function."""
    assert hello() == 'Hello you from cvo260922!'
