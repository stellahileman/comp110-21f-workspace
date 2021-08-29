"""Inputting numbers and showing how they work in Python"""

__author__ = "730400423"

left_original: str = input("Choose your first number ")
right_original: str = input("Choose your second number ")

left_hand: int = int(left_original)
right_hand: int = int(right_original)

exponent: float = left_hand ** right_hand
divide: float = left_hand / right_hand
integer_divide: float = left_hand // right_hand
remainder_divide: float = left_hand % right_hand

print("Left-hand side: " + left_original)
print("Right-hand side: " + right_original)

print(left_original + " ** " + right_original + " is " + str(exponent))
print(left_original + " / " + right_original + " is " + str(divide))
print(left_original + " // " + right_original + " is " + str(integer_divide))
print(left_original + " % " + right_original + " is " + str(remainder_divide))