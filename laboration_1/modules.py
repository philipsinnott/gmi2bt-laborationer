# Laboration 1 i GMI2BT

from random import randint
import statistics

def function_one(num1, num2):
    numbers = []

    while True:
        try:
            num1 = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input, please try again.")
    while True:
        try:
            num2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input, please try again.")

    for i in range(1, 1001):
        if i % num1 == 0 and i % num2 == 0:
            numbers.append(i)
    print(numbers)

    numbers_median = statistics.median(numbers)
    print(f"The median value is {numbers_median}.")

def guess_num():
    guess_count = 0
    secret_num = randint(1, 101)
    user_guess = 0
    max_guesses = 5

    while user_guess != secret_num and guess_count != max_guesses:
        while True:
            try:
                user_guess = int(input("Guess the number between 1-100: "))
                break
            except ValueError:
                print("Invalid input, please try again.")
        if user_guess > secret_num:
            guess_count += 1
            print(f"Too high, please try again. {guess_count}/{max_guesses} attempts done.")
        elif user_guess < secret_num:
            guess_count += 1
            print(f"Too low, please try again. {guess_count}/{max_guesses} attempts done.")
        elif user_guess == secret_num:
            guess_count += 1
            if guess_count > 1:
                print(f"Congratulations, you guessed the correct number ({secret_num}). It took you {guess_count} tries.")
            else:
                print(f"Congratulations, you guessed the correct number on your first try!\n"
                      "Consider joining the lottery.")
            break

def menu():

    choice = input("[1]: Function 1\n"
                   "[2]: Guess the number!\n"
                   "[3]: Exit\n"
                   "Choose what you want to do: ")
    if choice == "1":
        print()
        function_one(num1 = 0, num2 = 0)
    elif choice == "2":
        print()
        guess_num()
    elif choice == "3":
        print("Au revoir.")
        exit()
    else:
        print("Invalid input, please choose a valid option (1-3).")
        menu()
