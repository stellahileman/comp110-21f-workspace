"""An exercise in remainders and boolean logic."""

__author__ = "730400423"


number: int = int(input("Enter an int: "))

two: int = (number % 2)
seven: int = (number % 7)

if two != 0:
    if seven != 0:
        print("CAROLINA")
    else:
        print("HEELS")
else:
    if seven == 0:
        print("TAR HEELS")
    else:
        print("TAR")