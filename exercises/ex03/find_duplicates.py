"""Finding duplicate letters in a word!"""

__author__ = "730400423"


def find_duplicate(word: str) -> bool:
    """To find a duplicate letter"""
    pos_start: int = 0
    while pos_start < (len(word) - 1):
        pos_search = pos_start + 1
        while pos_search < len(word):
            if word[pos_start] == word[pos_search]:
                return True
            pos_search = pos_search + 1
        pos_start = pos_start + 1
    return False


word: str = input("Enter a word: ")

print("Found duplicate: " + str(find_duplicate(word)))
