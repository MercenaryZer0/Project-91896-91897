"""This is a Shape Calculator that provides functions to calculate the area and perimeter of a shape."""

import time  # Imports the time module
import math  # Imports the math module


# Function goes here
class Task:
    def __init__(self, rectangle, circle, triangle, parallelogram=False):
        self.rectangle = rectangle
        self.circle = circle
        self.triangle = triangle
        self.parallelogram = parallelogram


class ShapeCalculator:
    def __init__(self):
        self.history = []

    def rectangle(self, length, width):
        perimeter = 2 * (length + width)
        area = length * width

        self.history.append((f"Rectangle: Length = {length}, Width = {width}, area, perimeter"))
        return area, perimeter

    def circle(self, radius):
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius

        self.history.append((f"Circle: Radius = {radius}, Circumference = {circumference}, area, perimeter"))
        return area, circumference

    def triangle(self, a, b, c, base, height):
        perimeter = base + a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - base) * (s - a) * (s - b) * (s - b))

        self.history.append((f"Triangle: a = {a}, b = {b}, c = {c}, Base = {base}, Height = {height}, area, perimeter"))
        return area, perimeter
    
    def parallelogram(self, base, height, side):
        perimeter = 2 * (base + side)
        area = base * height

        self.history.append((f"Parallelogram: Side = {side}, Base = {base}, Height = {height}, area, perimeter"))
        return area, perimeter
    
    def view_history(self):
        if not self.history:
            print("No Task Found.")

        else:
            print("Active History")
            for item in self.history:
                print(f"{item[0]} - Area: {item[1]}, Perimeter: {item[2]}")
    
def not_blank(question):
    while True:
        response = input(question)

        if response == '':
            print("\nSorry, but this can't be blank. Please try again.")

        else:
            return response    

# Main routine goes here
def main_menu():
    shape_calc = ShapeCalculator()

    while True:
        print("\n Pick a shape")
        time.sleep(1)
        print("1. Rectangle")
        time.sleep(0.1)
        print("2. Circle")
        time.sleep(0.1)
        print("3. Triangle")
        time.sleep(0.1)
        print("4. Parallelogram")
        time.sleep(0.1)
        print("5. Show History")
        time.sleep(0.1)
        print("6. Exit")

        choice = not_blank("Enter your choice (1/2/3/4/5/6): ").lower()
        try:
            if choice == '1' or choice == 'Rectangle':
                choice = '1'
        
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))

                area, perimeter = shape_calc.rectangle(length, width)
                print(f"Area: {area}, Perimeter: {perimeter}")

            elif choice == '2' or choice == 'Circle':
                choice = '2'

                radius = float(input("Enter the radius of the circle: "))

                area, circumference = shape_calc.circle(radius)
                print(f"Area: {radius}, Circumference: {circumference}")

            elif choice == '3' or choice == 'Triangle':
                choice = '3'

                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                a = float(input("Enter the length of side a: "))
                b = float(input("Enter the length of side b: "))
                c = float(input("Enter the length of side c: "))

                area, perimeter = shape_calc.triangle(base, height, a, b, c)
                print(f"Area: {area}, Perimeter: {perimeter}")

            elif choice == '4' or choice == 'Parallelogram':
                choice = '4'

                base = float(input("Enter the base of the parallelogram: "))
                height = float(input("Enter the height of the parallelogram: "))
                side = float(input("Enter the length of the side: "))

                area, perimeter = shape_calc.parallelogram(base, height, side)
                print(f"Area: {area}, Perimeter: {perimeter}")

            elif choice == '5' or choice == 'Show History':
                choice = '5'
                shape_calc.view_history()

            elif choice == '6' or choice == 'Exit':
                choice == '6'
                print("Exiting...")
                time.sleep(3)
                print("Have a nice day.")
                break

            else:
                print("Invalid input. Please try again")

        except ValueError:
            print("Invalid input, must be a number. Please try again.")

if __name__ == '__main__':
    main_menu()
