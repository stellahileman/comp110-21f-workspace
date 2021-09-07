"""Repeating a beat in a loop."""

__author__ = "730400423"

sound: str = (input("What beat do you want me to repeat? "))
times: int = int(input("How many times do you want me to repeat it? "))
original: int = 2
final: str = ""

if times <= 0:
    print("No beat...")
else:
    while original <= times:
        final = str(final + sound + " ")
        original = original + 1

final = final + sound
print(final)