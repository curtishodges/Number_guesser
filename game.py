import random


def welcome():
    print("Welcome to number guesser V1.0")
    user_name = input("Can i get your name? ".lower())
    game_choice = input("Hello " + user_name + " would you like to guess a number (1) or have the computer guess your "
                                               "number? (2) ")
    if game_choice == "1":
        guess(0)
    if game_choice == "2":
        level_select = input("Please choose your level: 1(num 1 - 10) 2(num 1 - 20) 3(num 1 - 100) ")
        if level_select == "1":
            computer_guess(10)
        if level_select == "2":
            computer_guess(20)
        if level_select == "3":
            computer_guess(100)
    else:
        print("Sorry, please select 1 or 2 to choose your game mode")


def guess(x):
    x = input(" Please select your level: 1(num 1 - 10) 2(num 1 - 20) 3(num 1 - 100): ")
    if x == "1":
        random_number = random.randint(1, 10)
        guess = 0
        attempt = 0
        while guess != random_number:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < random_number:
                print("Sorry, guess again. Too low. ")
                attempt = attempt + 1
                print("You have guessed " + str(attempt) + " time(s)")
            elif guess > random_number:
                print("Sorry, guess again. Too high")
                attempt = attempt + 1
                print("You have guessed " + str(attempt) + " time(s)")
        print(f"Congratulations, you have guessed the number {random_number} !")
        print("You took " + str(attempt) + " attempts to guess correctly")
    if x == "2":
        random_number = random.randint(1, 20)
        guess = 0
        attempt = 0
        while guess != random_number:
            guess = int(input("Guess a number between 1 and 20: "))
            if guess < random_number:
                print("Sorry, guess again. Too low. ")
                attempt = attempt + 1
                print("You have guessed " + str(attempt) + " time(s)")
            elif guess > random_number:
                print("Sorry, guess again. Too high")
                attempt = attempt + 1
                print("You have guessed " + str(attempt) + " time(s)")
        print(f"Congratulations, you have guessed the number {random_number} !")
        print("You took " + str(attempt) + " attempts to guess correctly")
    if x == "3":
        random_number = random.randint(1, 100)
        guess = 0
        attempt = 0
        while guess != random_number:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < random_number:
                print("Sorry, guess again. Too low. ")
                attempt = attempt + 1
                print("You have guessed " + str(attempt) + " time(s)")
            elif guess > random_number:
                print("Sorry, guess again. Too high")
                attempt = attempt + 1
                print("You have guessed " + str(attempt) + " time(s)")
        print(f"Congratulations, you have guessed the number {random_number} !")
        print("You took " + str(attempt) + " attempts to guess correctly")


def computer_guess(i):
    low = 1
    high = i
    feedback = " "
    attempt = 0
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?? ".lower())
        if feedback == "h":
            high = guess - 1
            attempt = attempt + 1
        elif feedback == "l":
            low = guess + 1
            attempt = attempt + 1
    print(f"The computer guessed your number, your number is {guess}")
    print("it took the computer " + str(attempt) + " attempts to guess your number")


welcome()
