import time # Imports the time module
import math # Imports the math module

# Function goes here
class Task:
    def __init__(self, rectangle, circle, triangle, parallelogram = False):
        self.rectangle = rectangle
        self.circle = circle
        self.triangle = triangle
        self.parallelogram = parallelogram

class ShapeCalculator:
    def __init__(self):
        self.history = []

    def calc_rectangle(self, length, width):
        

    def calc_circle(self):


    def calc_triangle(self):


    def calc_parallelogram(self):

    
def not_blank(question):
    while True:
        response = input(question)

        if response == '':
            print("Sorry, but this can't be blank. Please try again.")

        else:
            return response    

# Main routine goes here
def main_menu(self):
    shape_calc = ShapeCalculator()

    while True:
        print("\n Pick a shape")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Parallelogram")
        print("5. Exit")

        choice = not_blank("Enter your choice (1/2/3/4/5): ").lower()

        if choice == '1' or choice == 'Rectangle':
            choice = '1'
            shape_calc.calc_rectangle()

        elif choice == '2' or choice == 'Circle':
            choice = '2'
            shape_calc.calc_circle

        elif choice == '3' or choice == 'Triangle':
            choice = '3'
            shape_calc.calc_triangle

        elif choice == '4' or choice == 'Parallelogram':
            choice = '4'
            shape_calc.calc_parallelogram

        elif choice == '5' or choice == 'Exit':
            choice == '5'
            print("Exiting...")
            time.sleep(3)
            break

        else:
            print("Invalid input. Please try again")

if __name__ == '__main__':
    main_menu()