"""More operators, but this time comparing"""

__author__ = "730400423"

left_original: str = input("Choose your first number ")
right_original: str = input("Choose your second number ")

left_hand: int = int(left_original)
right_hand: int = int(right_original)

less_than: bool = left_hand < right_hand
at_least: bool = left_hand >= right_hand
equal_to: bool = left_hand == right_hand
not_equal: bool = left_hand != right_hand

print("Left-hand side: " + left_original)
print("Right-hand side: " + right_original)

print(left_original + " < " + right_original + " is " + str(less_than))
print(left_original + " >= " + right_original + " is " + str(at_least))
print(left_original + " == " + right_original + " is " + str(equal_to))
print(left_original + " != " + right_original + " is " + str(not_equal))