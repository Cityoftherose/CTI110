# Simple Math Quizzes that test user's addition and subtraction skills
# 12/3/23
# CTI-110 P5HW - Math Quiz
# Aletha Holmes
#


# import random module
import random

# Define a function to generate two random numbers between 1 and 100
def generate_numbers():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return number1, number2

# Define a function to ask the user to add two numbers and check the answer
def add_numbers():
    # Get the numbers and the correct answer
    number1, number2 = generate_numbers()
    result = number1 + number2
    # Display the problem and get the user's guess
    guess = int(input(f"  {number1}\n+ {number2}\n\nEnter answer. \n"))
    # Initialize the number of guesses
    count = 1
    # Loop until the guess is correct
    while guess != result:
        # Give feedback based on the guess
        if guess < result:
            guess = int(input("Sorry, guess is too low.\n \nTry again: "))
        else:
            guess = int(input("Sorry, guess is too high.\n \nTry again: "))
        # Increment the number of guesses
        count += 1
    # Congratulate the user and show the number of guesses
    print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {count}")

# Define a function to ask the user to subtract two numbers and check the answer
def subtract_numbers():
    # Get the numbers and the correct answer
    number1, number2 = generate_numbers()
    # Make sure the first number is larger than the second
    if number1 < number2:
        number1, number2 = number2, number1
    result = number1 - number2
    # Display the problem and get the user's guess
    guess = int(input(f"  {number1}\n- {number2}\n\nEnter answer. \n"))
    # Initialize the number of guesses
    count = 1
    # Loop until the guess is correct
    while guess != result:
        # Give feedback based on the guess
        guess = int(input("Sorry, guess is incorrect.\n \nTry again: "))
        # Increment the number of guesses
        count += 1
    # Congratulate the user and show the number of guesses
    print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {count}")

# Define a function to display the main menu and get the user's choice
def display_menu():
    print("\nMAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    # Get the user's choice and validate it
    choice = input("\nPlease choose one of the menu options: ")
    while choice not in ["1", "2", "3"]:
        print("\nError: Invalid choice. Please choose again.")
        choice = input("\nPlease choose one of the menu options: ")
    return choice

# Define the main function
def main():
    # Welcome the user
    print("Welcome to Math Quiz")
    # Loop until the user chooses to exit
    while True:
        # Get the user's choice from the menu
        choice = display_menu()
        # Call the appropriate function based on the choice
        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            # Thank the user and exit the loop
            print("Thank you for playing...\nBye!!")
            break

# Call the main function
if __name__ == "__main__":
    main()
