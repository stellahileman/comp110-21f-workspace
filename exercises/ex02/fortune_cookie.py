"""Program that outputs one of at least four random, good fortunes."""
from random import randint
__author__ = "730400423"

print("Your fortune cookie says... ")
sentence_number: int = int(randint(1, 4))

if sentence_number == 1:
    print("You will find a 20 dollar bill on the ground!")
else:
    if sentence_number == 2:
        print("You will make a new friend today!")
    else:
        if sentence_number == 3:
            print("You will lose one airpod :(")
        else:
            if sentence_number == 4:
                print("You will meet your soulmate at Lenoir!")
            else:
                print(" ")

print("Now, go spread positive vibes!")