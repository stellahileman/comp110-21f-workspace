"""Practice with dictionaries."""

__author__ = "730400423"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the items in a dictionary."""
    output = dict()
    for key in dictionary:
        if dictionary[key] in output:
            raise KeyError("duplicates found")
        output[dictionary[key]] = key
    return output


def favorite_color(dictionary: dict[str, str]) -> str:
    """Finds color that is most frequent in a dictionary."""
    color_counts: dict[str, int] = {}
    for key in dictionary:
        if dictionary[key] in color_counts:
            color_counts[dictionary[key]] = color_counts[dictionary[key]] + 1
        else:
            color_counts[dictionary[key]] = 1
    max_count: int = 0
    fav_color: str = ""
    for color in color_counts:
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            fav_color = color
    return fav_color
        

def count(given: list[str]) -> dict[str, int]:
    """Produces a dictionary from a list that counts how many times a value appears."""
    counts: dict[str, int] = {}
    for value in given:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts