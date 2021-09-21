"""Choose your own adventure, getting to class style!"""

points: int = 0
player: str = input("Hey! Welcome to the game! To get started I first have to know your name: ")


def main() -> None:
    greet()
    print("BEEP! BEEP! BEEP!")
    print(f"Good morning {player}!")
    print("How do you want to start your day?")
    print("a. snooze the alarm \U000023F0")
    print("b. jump out of bed \U0001F6CF")
    print("c. make some coffee \U00002615")
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
    print(f"Welcome {player}, let me tell you how this game works!")
    print("Throughout the game you will be faced with three choices: a, b, or c.")
    print("Type your choice's corresponding letter after each set of answers.")
    print("To accumulate player points you must choose the smartest options, or you can just have fun!")
    print("OK! Let the games begin!!")
    print(" ")


# First Choice Answers
def snooze() -> None:
    global points
    points = points + 1
    print(f"You have {points} player points.")
    print(" ")
    print("Alright go back to sleep then")
    print("...")
    print("BEEP! BEEP! BEEP!")
    print("DUDE! You have fifteen minutes to leave for class!!! Get up!")
    print("What should you do first? ")
    print("a. brush your teeth \U0001F9B7")
    print("b. get dressed \U0001F455")
    print("c. get that last minute studying done \U0001F4D4")
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
    print(f"You have {points} player points.")
    print(" ")
    print("C'mon " + player + "! Did you really forget that you lofted your bed??")
    print("Now we have to take you to student health, good luck getting to class now.")


def coffee() -> None:
    global points
    points = points + 2
    print(f"You have {points} player points.")
    print(" ")
    print("Mmmmm... smells so good")
    print("What a lovely morning, what do you want to do next?")
    print("a. play some good wake-up music \U0001F3B6")
    print("b. get some last-minute studying in \U0001F4D4")
    print("c. take a shower \U0001F6BF")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            music()
        if choice == "b":
            loop = 2
            studying_earlier()
        if choice == "c":
            loop = 2
            shower()
        else:
            print("You did not choose an answer!!! Try again. This time type either a, b, or c.")


# Snooze Answers
def teeth() -> None:
    global points
    points = points + 1
    print(f"You have {points} player points.")
    print(" ")
    print("You try to open the bathroom door and...")
    print("What??? It is locked! Someone is taking a shower!")
    print("Should you")
    print("a. use the lobby bathroom to brush your teeth \U0001F9B7")
    print("b. get dressed \U0001F455")
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
    print(f"You have {points} player points.")
    print(" ")
    print("Ok nice, one thing done.")
    print("What is next??")
    print("a. some last minute studying \U0001F4D4")
    print("b. brushing teeth \U0001F9B7")
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
    print(f"You have {points} player points.")
    print(" ")
    print("Not sure how much work you can really get done before school...")
    print("15 minutes later")
    print(f"{player} you barely opened your textbook! And you have to leave now!!!")
    print("I am sorry bro, you can't make it to class looking like that.")


# Teeth Answer
def lobby() -> None:
    global points
    points = points + 1
    print(f"You have {points} player points.")
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
    print(f"You have {points} player points.")
    print(" ")
    print("OK Thank god the door is open now!")
    print("Man, you gotta get out the door STAT!")
    hurried()


# For when about to be late
def hurried() -> None:
    global points
    points = points + 1
    print(f"You have {points} player points.")
    print(" ")
    print("OK, don't forget the keys!")
    print("Ten minutes later...")
    print("We barely made it to Hamilton Hall!")
    print("But wait, who is that at the door??")
    print("MYSTERIOUS MAN- YOU CANNOT PASS WITHOUT A PASSWORD!")
    print("Hmmmm... looks like when we are late we have to guess the right number to get into class!")
    print("IT WILL BE A NUMBER ONE TO TEN")
    print("MYSTERIOUS MAN- WOULD YOU LIKE:")
    print("a. YOUR COMPUTER FRIEND TO CHOOSE A NUMBER \U0001F5A5")
    print("OR b. CHOOSE A NUMBER YOURSELF \U00002696")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            guess = computer()
        if choice == "b":
            loop = 2
            guess = choose()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")
    if guess == 7:
        print("YOU GUESSED IT YOU CAN PASS.")
        print("Great job you made it to class!!")
    else:
        print("YOU FAILED.")
    

def computer() -> int:
    from random import randint
    guess: int = randint(1, 10)
    print(f"I guessed {guess}")
    return guess


def choose() -> int:
    guess: int = int(input("Choose a number: "))
    print(f"You guessed {guess}")
    return guess


# Coffee Answers
def music() -> None:
    global points
    points = points - 1
    print(f"You have {points} player points.")
    print(" ")
    print("Uhhhh... is Pitbull really how you wake up?")
    print("Look your roommate woke up! And they don't look too happy about this.")
    print("Uh oh here comes a punch")
    print("BAM!")
    print("Can't go to class with a bloody nose...")
    print("Looks like it is time for a trip to Campus Health instead.")


def studying_earlier() -> None:
    global points
    points = points + 1
    print(f"You have {points} player points.")
    print(" ")
    print("Ok it looks like you have enough time to get some studying done!")
    print("...")
    print("Wow you finished that entire COMP 110 assignment?!? ")
    print("What would you like to do next?")
    print("a. get dressed \U0001F455")
    print("b. shower \U0001F6BF")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            dressed_early()
        if choice == "b":
            loop = 2
            shower()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")


def shower() -> None:
    global points
    points = points + 2
    print(f"You have {points} player points.")
    print(" ")
    print("Good choice!")
    print("...")
    print("OK what is next?")
    print("a. get dressed \U0001F455")
    print("b. brush teeth \U0001F9B7")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            dressed_early()
        if choice == "b":
            loop = 2
            early_teeth()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")


# Studying early answer
def dressed_early() -> None:
    global points
    points = points + 2
    print(f"You have {points} player points.")
    print(" ")
    print(f"Nice outfit {player}!")
    print("Hmmmm... anything else before we go to school?")
    print("Uh oh your breath still stinks let's take care of that!")
    print("...")
    print("Wow nice pearly whites!")
    print("But we have to get out the door!!")
    class_on_time()


def early_teeth() -> None:
    global points
    points = points + 2
    print(f"You have {points} player points.")
    print(" ")
    print("Nice pearly whites! But we gotta get dressed still!")
    print(f"Solid fit {player}!")
    print("Let's get out the door!")
    class_on_time()


def class_on_time() -> None:
    global points
    points = points + 3
    print(f"You have {points} player points.")
    print(" ")
    print("Wow great job getting to class on time!")
    print("You look ready to learn about strings and lists now!")


print(str(points))

if __name__ == "__main__":
    main()