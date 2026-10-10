
import random


# Tool 1: A calculator that performs basic arithmetic.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = first_number / second_number
        else:
            print(f"Sorry, '{operator}' is not a valid operation.")
            return

        print(f"The answer is: {result:g}")

    except ValueError:
        print("Please enter valid numbers and try again.")


# Tool 2: A guessing game that repeats until the user wins.
def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    attempts = 0

    print("I have chosen a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Correct! You guessed the number in "
                    f"{attempts} attempt(s)."
                )
                break

        except ValueError:
            print("Please enter a whole number.")


# Tool 3: A to-do list that changes as tasks are added or removed.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Your task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(
                    input("Enter the task number to remove: ")
                )

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Removed task: {removed_task}")
                else:
                    print("That task number does not exist.")

            except ValueError:
                print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


# Tool 4: A name formatter that displays different letter cases.
def name_formatter():
    print("\n--- Name Formatter ---")
    name = input("Enter your full name: ").strip()

    if not name:
        print("Please enter a name.")
    else:
        print(f"Original name: {name}")
        print(f"Uppercase: {name.upper()}")
        print(f"Lowercase: {name.lower()}")
        print(f"Title case: {name.title()}")


# Main menu: Repeats until the user chooses to quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. Number Guessing Game")
        print("3. To-Do List")
        print("4. Name Formatter")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            number_guessing_game()
        elif choice == "3":
            todo_list()
        elif choice == "4":
            name_formatter()
        elif choice == "5":
            print("Thank you for using my toolkit. Goodbye!")
            break
        else:
            print(
                f"Sorry, '{choice}' is not a valid choice. "
                "Please enter a number from 1 to 5."
            )


if __name__ == "__main__":
    main()
