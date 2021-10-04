"""List utility functions."""

__author__ = "730400423"


def all(a: list[int], b: int) -> bool:
    """Finding out if a given integer is all the items in the list."""
    i = 0
    if len(a) == 0:
        return False
    else:
        while i < len(a):
            if a[i] == b:
                i += 1
            else:
                return False
        return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """Finding out if both lists have the exact same values."""
    a_length: int = len(a)
    b_length: int = len(b)
    if a_length == 0 and b_length == 0:
        return True
    else:
        i = 0
        if a_length == b_length:
            if a_length <= len(b):
                while i < a_length:
                    if a[i] == b[i]:
                        return True
                    else:
                        i += 1
                return False
            else:
                while i < b_length:
                    if a[i] == b[i]:
                        return True
                    else:
                        i += 1
                return False
        else:
            return False


def max(input: list[int]) -> int:
    """Finding which value is the highest."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    most: int = input[0]
    n: int = 1
    while n < len(input):
        if input[n] > most:
            most = input[n]
        n += 1  
    return most