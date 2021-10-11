"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730400423"


def test_empty_list() -> None:
    """Testing if all functions return empty lists when given an empty list."""
    a: list[int] = []
    assert only_evens(a) == []
    assert sub(a, 1, 3) == []
    assert concat(a, []) == []


def test_many_items() -> None:
    """Testing if all functions work when given a large amount of numbers."""
    a: list[int] = [1, 2, 40, 39]
    assert only_evens(a) == [2, 40]
    assert sub(a, 1, 3) == [2, 40]
    assert concat(a, [4, 7, 30]) == [1, 2, 40, 39, 4, 7, 30]


def test_two_items() -> None:
    """Testing if all functions work when given two numberes."""
    a: list[int] = [40, 29]
    assert only_evens(a) == [40]
    assert sub(a, 0, 1) == [40]
    assert concat(a, [2, 30, 17]) == [40, 29, 2, 30, 17]