# Function goes here...
import time

# Comment.
def main_menu(self):
    while True:
        print("1. Shop")
        print("2. Instructions")
        print("3. Exit")

        # Ask the user to choose among the following choices
        choice = input("Enter your choice")

        # if user inputs 1, program continues
        if choice == '1':
            time.sleep(1)

        # if user inputs 2, the program will display instructions
        elif choice == '2':
            print("Instructions go here.")
            continue

        # if user inputs 3, program ends
        elif choice == '3':
            print("Have a nice day!")
            break

        # if user inputs anything else, 
        else:
            print("Sorry, I didn't quite get that. Please try again")

# Main routine goes here...
print("test commit")
