"""Choose your own adventure, getting to class style!"""

points: int = 0
player: str = input("Hey! Welcome to the game! To get started I first have to know your name: ")


def main() -> None:
    greet()
    print("BEEP! BEEP! BEEP!")
    print("Good morning " + player + "!")
    print("How do you want to start your day?")
    print("a. snooze the alarm")
    print("b. jump out of bed")
    print("c. make some coffee")
    choice_one: str = input("Make your choice here: ")
    if choice_one == "a":
        snooze()
    if choice_one == "b":
        jump()
    if choice_one == "c":
        coffee()


def greet() -> None:
    print(" ")
    print("Welcome " + player + ", let me tell you how this game works!")
    print("Throughout the game you will be faced with three choices: a, b, or c.")
    print("Type your choice's corresponding letter after each set of answers.")
    print("To accumulate player points you must choose the smartest options, or you can just have fun!")
    print("OK! Let the games begin!!")
    print(" ")


def snooze() -> None:
    global points
    points = points + 1
    print(" ")
    print("Alright go back to sleep then")
    print("...")
    print("BEEP! BEEP! BEEP!")
    print("DUDE! You have fifteen minutes to leave for class!!! Get up!")
    print("What should you do first? ")
    print("a. brush your teeth")
    print("b. get dressed")
    print("c. get that last minute studying done")


def jump() -> None:
    global points
    points = points - 1
    print(" ")
    print("C'mon " + player + "! Did you really forget that you lofted your bed??")
    print("Now we have to take you to student health, good luck getting to class now.")


def coffee() -> None:
    global points
    points = points + 2
    print(" ")
    print("Mmmmm... smells so good")
    print("What a lovely morning, what do you want to do next?")
    print("a. play some good wake-up music")
    print("b. get some last-minute studying in")
    print("c. take a shower")


print(str(points))

if __name__ == "__main__":
    main()