# Function goes here...
def main_menu(self):
    while True:
        print("1. Start")
        print("2. Exit")
        choice = input("Enter your choice: ")

        # If user inputs 1, the loop begins
        if choice == 1:
            print("You may continue")
            continue

        # If the user inputs 2, the program prints a message and then ends
        elif choice == 2:
            print("Thank you for your time.")
            break

        else:
            print("Invalid choice. Please try again")

# Main Routine goes here...
