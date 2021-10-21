"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730400423"


def test_empty_dict_colors_invert() -> None:
    """Testing that the first two functions return blank lines when given blank dictionaries."""
    test: dict[str, str] = {}
    assert invert(test) == {}
    assert favorite_color(test) == ""


def test_empty_list_count() -> None:
    """Testing that the last function returns a blank dictionary when given a blank list."""
    test: list[str] = []
    assert count(test) == {}


def test_long_dict_invert() -> None:
    """Testing that invert works when given a long dictionary."""
    test: dict[str, str] = {"Stella": "Green", "River": "Blue", "Claudia": "Yellow", "Everett": "Purple", "Phil": "Pink", "Max": "Red"}
    assert invert(test) == {"Green": "Stella", "Blue": "River", "Yellow": "Claudia", "Purple": "Everett", "Pink": "Phil", "Red": "Max"}


def test_long_dict_colors() -> None:
    """Testing that color works when given a long dictionary."""
    test: dict[str, str] = {"Stella": "Green", "River": "Blue", "Claudia": "Yellow", "Everett": "Green", "Phil": "Blue", "Max": "Green"}
    assert favorite_color(test) == "Green"


def test_long_list_count() -> None:
    """Testing that count works when given a long list."""
    test: list[str] = ["Green", "Blue", "Pink", "Blue", "Green", "Green"]
    assert count(test) == {"Green": 3, "Blue": 2, "Pink": 1}


def test_short_dict_invert() -> None:
    """Testing that invert still works when given a short list."""
    test: dict[str, str] = {"Stella": "Green"}
    assert invert(test) == {"Green": "Stella"}


def test_short_dict_colors() -> None:
    """Testing that color still works when given a short list."""
    test: dict[str, str] = {"Stella": "Green"}
    assert favorite_color(test) == "Green"


def test_short_list_count() -> None:
    """Testing that count still works when given a short list."""
    test: list[str] = ["Green"]
    assert count(test) == {"Green": 1}