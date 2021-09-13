"""Drawing forests in a loop."""

__author__ = "730400423"


TREE: str = '\U0001F332'
number: int = int(input("Depth: "))
first: int = 1

if number >= 0:
    while first <= number:
        print(TREE + ((TREE) * (first - 1)))
        first = first + 1
