"""Counting letters in a string."""

__author__ = "730400423"

letter: str = input("What letter do you want to search for: ")
word: str = input("Enter a word: ")
length: int = len(word)
count: int = 0
pos: int = 0

while pos < length:
    if letter == word[pos]:
        count = count + 1
    pos = pos + 1

print("Count: " + str(count))