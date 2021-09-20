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
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            snooze()
        if choice == "b":
            loop = 2
            jump()
        if choice == "c":
            loop = 2
            coffee()
        else:
            print("You did not choose an answer!!! Try again. This time type either a, b, or c.")


def greet() -> None:
    print(" ")
    print("Welcome " + player + ", let me tell you how this game works!")
    print("Throughout the game you will be faced with three choices: a, b, or c.")
    print("Type your choice's corresponding letter after each set of answers.")
    print("To accumulate player points you must choose the smartest options, or you can just have fun!")
    print("OK! Let the games begin!!")
    print(" ")


# First Choice Answers
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
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            teeth()
        if choice == "b":
            loop = 2
            dressed()
        if choice == "c":
            loop = 2
            studying_early()
        else:
            print("You did not choose an answer!!! Try again. This time type either a, b, or c.")


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


# Snooze Answers
def teeth() -> None:
    global points
    points = points + 1
    print(" ")
    print("You try to open the bathroom door and...")
    print("What??? It is locked! Someone is taking a shower!")
    print("Should you")
    print("a. use the lobby bathroom to brush your teeth")
    print("b. get dressed")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            lobby()
        if choice == "b":
            loop = 2
            dressed()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")


def dressed() -> None:
    global points
    points = points + 2
    print(" ")
    print("Ok nice, one thing done.")
    print("What is next??")
    print("a. some last minute studying")
    print("b. brushing teeth")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            studying_early()
        if choice == "b":
            loop = 2
            later_teeth()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")


def studying_early() -> None:
    global points
    points = points - 1
    print(" ")
    print("Not sure how much work you can really get done before school...")
    print("15 minutes later")
    print(player + ", you barely opened your textbook! And you have to leave now!!!")
    print("I am sorry bro, you can't make it to class looking like that.")


# Teeth Answer
def lobby() -> None:
    global points
    points = points + 1
    print(" ")
    print("OK at least you made it to A bathroom.")
    print("Not the cleanest, but it will do.")
    print("You only have a few minutes now!!! Time to get dressed!")
    print("Kinda a weird outfit, but will have to do")
    print("Gotta get out the door!")
    hurried()


# Dressed Answer
def later_teeth() -> None:
    global points
    points = points + 1
    print(" ")
    print("OK Thank god the door is open now!")
    print("Man, you gotta get out the door STAT!")
    hurried()


# For when about to be late
def hurried() -> None:
    print(" ")
    print("OK, don't forget the keys!")
    print("Ten minutes later...")
    print("We barely made it to Hamilton Hall!")
    print("But wait, who is that at the door??")
    print("MYSTERIOUS MAN- YOU CANNOT PASS WITHOUT A PASSWORD!")
    print("Hmmmm... looks like when we are late we have to guess the right number to get into class!")
    print("MYSTERIOUS MAN- WOULD YOU LIKE:")
    print("a. YOUR COMPUTER FRIEND TO CHOOSE A NUMBER")
    print("OR b. CHOOSE A NUMBER YOURSELF")
   
    
print(str(points))

if __name__ == "__main__":
    main()