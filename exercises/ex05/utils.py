"""List utility functions part 2."""

__author__ = "730400423"


def only_evens(a: list[int]) -> list[int]:
    """Finding which values in a list are even."""
    output: list[int] = []
    i = 0
    while i < len(a):
        if (a[i] % 2) == 0:
            output.append(a[i])
        i += 1
    return output


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Repeating values in a list with two parameters."""
    output: list[int] = []
    pos: int = b
    if pos < 0:
        pos = 0
    while pos < c and pos < len(a):
        output.append(a[pos])
        pos += 1
    return output


def concat(a: list[int], b: list[int]) -> list[int]:
    """Adding two lists together."""
    c: list[int] = a + b
    return c