"""Choose your own adventure, getting to class style!"""

__author__ = "730400423"

player: str

# Emojis
CLOCK: str = '\U000023F0'
BED: str = '\U0001F6CF'
COFFEE: str = '\U00002615'
TEETH: str = '\U0001F9B7'
DRESSED: str = '\U0001F455'
BOOK: str = '\U0001F4D4'
MUSIC: str = '\U0001F3B6'
SHOWER: str = '\U0001F6BF'
COMPUTER: str = '\U0001F5A5'
SCALE: str = '\U00002696'


def main() -> None:
    """To start off the game."""
    global points
    points: int = 0
    greet()
    redo = 1
    while redo == 1:
        print("BEEP! BEEP! BEEP!")
        print(f"Good morning {player}!")
        print("How do you want to start your day?")
        print(f"a. snooze the alarm {CLOCK}")
        print(f"b. jump out of bed {BED}")
        print(f"c. make some coffee {COFFEE}")
        loop = 0
        while loop < 1:
            choice: str = input("Make your choice here: ")
            if choice == "a":
                loop = 2
                snooze()
            elif choice == "b":
                loop = 2
                jump()
            elif choice == "c":
                loop = 2
                coffee()
            else:
                print("You did not choose an answer!!! Try again. This time type either a, b, or c.")
        print(" ")
        print("Thanks for playing the game!")
        print("Let's see how you did!!")
        points_again: int = score(points)
        print(f"Do you want to try again? Maybe we can beat {points_again}")
        print("a. yes")
        print("b. no")
        loop = 0
        while loop < 1:
            choice: str = input("Make your choice here: ")
            if choice == "a":
                loop = 2
                redo = 1
            elif choice == "b":
                loop = 2
                print("Ok! See you later!")
                redo = 0
            else:
                print("You did not choose an answer!!! Try again. This time type either a or b")
        

def greet() -> None:
    """To introduce the instructions."""
    global player
    player = input("Hey! Welcome to the game! To get started I first have to know your name: ")
    print(" ")
    print(f"Welcome {player}, let me tell you how this game works!")
    print("Throughout the game you will be faced with three choices: a, b, or c.")
    print("Type your choice's corresponding letter after each set of answers.")
    print("To accumulate player points you must choose the smartest options, or you can just have fun!")
    print("OK! Let the games begin!!")
    print(" ")


# First Choice Answers
def snooze() -> None:
    """What if you snooze the alarm."""
    global points
    points = points + 1
    print(f"You have {points} player points.")
    print(" ")
    print("Alright go back to sleep then")
    print("...")
    print("BEEP! BEEP! BEEP!")
    print("DUDE! You have fifteen minutes to leave for class!!! Get up!")
    print("What should you do first? ")
    print(f"a. brush your teeth {TEETH}")
    print(f"b. get dressed {DRESSED}")
    print(f"c. get that last minute studying done {BOOK}")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            teeth()
        elif choice == "b":
            loop = 2
            dressed()
        elif choice == "c":
            loop = 2
            studying_early()
        else:
            print("You did not choose an answer!!! Try again. This time type either a, b, or c.")


def jump() -> None:
    """What if you jump out of bed."""
    global points
    global player
    points = points - 1
    print(f"You have {points} player points.")
    print(" ")
    print(f"C'mon {player} ! Did you really forget that you lofted your bed??")
    print("Now we have to take you to student health, good luck getting to class now.")


def coffee() -> None:
    """What if you start some coffee."""
    global points
    global player
    points = points + 2
    print(f"You have {points} player points.")
    print(" ")
    print("Mmmmm... smells so good")
    print("What a lovely morning, what do you want to do next?")
    print(f"a. play some good wake-up music {MUSIC}")
    print(f"b. get some last-minute studying in {BOOK}")
    print(f"c. take a shower {SHOWER}")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            music()
        elif choice == "b":
            loop = 2
            studying_earlier()
        elif choice == "c":
            loop = 2
            shower()
        else:
            print("You did not choose an answer!!! Try again. This time type either a, b, or c.")


# Snooze Answers
def teeth() -> None:
    """What if you snooze the alarm and try to brush your teeth."""
    global points
    points = points + 1
    print(f"You have {points} player points.")
    print(" ")
    print("You try to open the bathroom door and...")
    print("What??? It is locked! Someone is taking a shower!")
    print("Should you")
    print(f"a. use the lobby bathroom to brush your teeth {TEETH}")
    print(f"b. get dressed {DRESSED}")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            lobby()
        elif choice == "b":
            loop = 2
            dressed()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")


def dressed() -> None:
    """What if you snooze your alarm and then get dressed."""
    global points
    points = points + 2
    print(f"You have {points} player points.")
    print(" ")
    print("Ok nice, one thing done.")
    print("What is next??")
    print(f"a. some last minute studying {BOOK}")
    print(f"b. brushing teeth {TEETH}")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            studying_early()
        elif choice == "b":
            loop = 2
            later_teeth()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")


def studying_early() -> None:
    """What if you snooze your alarm and then try to get some studying done."""
    global points
    global player
    points = points - 1
    print(f"You have {points} player points.")
    print(" ")
    print("Not sure how much work you can really get done before school...")
    print("15 minutes later")
    print(f"{player} you barely opened your textbook! And you have to leave now!!!")
    print("I am sorry bro, you can't make it to class looking like that.")


# Teeth Answer
def lobby() -> None:
    """What if you snooze your alarm, try to brush your teeth, and then try again in the lobby."""
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
    """What if you snooze the alarm, get dressed, and brush your teeth."""
    global points
    points = points + 1
    print(f"You have {points} player points.")
    print(" ")
    print("OK Thank god the door is open now!")
    print("Man, you gotta get out the door STAT!")
    hurried()


# For when about to be late
def hurried() -> None:
    """What if you snooze the alarm and after getting ready only have 15 minutes to get to class."""
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
    print(f"a. YOUR COMPUTER FRIEND TO CHOOSE A NUMBER {COMPUTER}")
    print(f"OR b. CHOOSE A NUMBER YOURSELF {SCALE}")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            guess = computer()
        elif choice == "b":
            loop = 2
            guessed_number: int = int(input("Choose a number: "))
            guess = choose(guessed_number)
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")
    if guess == 7:
        print("YOU GUESSED IT YOU CAN PASS.")
        print("Great job you made it to class!!")
    else:
        print("YOU FAILED.")
        print("Guess you can't make it to class :(")
    

def computer() -> int:
    """Having the computer choose a random number."""
    from random import randint
    guess: int = randint(1, 10)
    print(f"I guessed {guess}")
    return guess


def choose(a: int) -> int:
    """The player choosing a number."""
    print(f"You guessed {a}")
    return a


# Coffee Answers
def music() -> None:
    """What if you get up and make some coffee."""
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
    """What if you get some early morning studying done."""
    global points
    points = points + 1
    print(f"You have {points} player points.")
    print(" ")
    print("Ok it looks like you have enough time to get some studying done!")
    print("...")
    print("Wow you finished that entire COMP 110 assignment?!? ")
    print("What would you like to do next?")
    print(f"a. get dressed {DRESSED}")
    print(f"b. shower {SHOWER}")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            dressed_early()
        elif choice == "b":
            loop = 2
            shower()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")


def shower() -> None:
    """What if you shower."""
    global points
    points = points + 2
    print(f"You have {points} player points.")
    print(" ")
    print("Good choice!")
    print("...")
    print("OK what is next?")
    print(f"a. get dressed {DRESSED}")
    print(f"b. brush teeth {TEETH}")
    loop = 0
    while loop < 1:
        choice: str = input("Make your choice here: ")
        if choice == "a":
            loop = 2
            dressed_early()
        elif choice == "b":
            loop = 2
            early_teeth()
        else:
            print("You did not choose an answer!!! Try again. This time type either a or b")


# Studying early answer
def dressed_early() -> None:
    """What if you study and then get dressed."""
    global points
    global player
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
    """What if you get up at a decent hour and brush your teeth."""
    global points
    global player
    points = points + 2
    print(f"You have {points} player points.")
    print(" ")
    print("Nice pearly whites! But we gotta get dressed still!")
    print(f"Solid fit {player}!")
    print("Let's get out the door!")
    class_on_time()


def class_on_time() -> None:
    """What if you get to class at a decent hour."""
    global points
    points = points + 3
    print(f"You have {points} player points.")
    print(" ")
    print("Wow great job getting to class on time!")
    print("You look ready to learn about strings and lists now!")


# Score
def score(a: int) -> int:
    """Calculating how well the player did."""
    print(f"Your final score is: {a}")
    if points >= 8:
        print("Wow great job!! You got a perfect score!")
    else:
        if points >= 6:
            print("Great job getting to class!")
        else:
            if points >= 3:
                print("Eh. You did ok")
            else:
                if points >= 0:
                    print("Uhhhh... you did not do so good bud.")
                else:
                    print("Wow!! Below 0?!?! That is impressive on it's own.")
    return a
    

if __name__ == "__main__":
    main()