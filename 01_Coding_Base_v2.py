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
        perimeter = 2 * (length + width)
        area = length * width

        self.history.append((f"Rectangle: Length = {length}, Width = {width}, area, perimeter"))
        return area, perimeter

    def calc_circle(self, radius):
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius

        self.history.append((f"Circle: Radius = {radius}, Circumference = {circumference}, area, perimeter"))
        return area, circumference
    

    def calc_triangle(self, a, b, c, base, height):
        perimeter = base + a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - base) * (s - a) * (s - b) * (s - b))


        self.history.append((f"Triangle: a = {a}, b = {b}, c = {c}, Base = {base}, Height = {height}, area, perimeter"))
        return area, perimeter

    def calc_parallelogram(self, base, height, side):
        perimeter = 2 * (base + side)
        area = base * height

        self.history.append((f"Parallelogram: Side = {side}, Base = {base}, Height = {height}, area, perimeter"))
        return area, perimeter
    
    def view_history(self):
        print("Active History")
        for item in self.history:
            print(f"{item[0]} - Area: {item[1]}, Perimeter: {item[2]}")
    
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
        time.sleep(2)
        print("1. Rectangle")
        time.sleep(1)
        print("2. Circle")
        time.sleep(1)
        print("3. Triangle")
        time.sleep(1)
        print("4. Parallelogram")
        time.sleep(1)
        print("5. Show History")
        time.sleep(1)
        print("6. Exit")

        choice = not_blank("Enter your choice (1/2/3/4/5/6): ").lower()

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

        elif choice == '5' or choice == 'Show History':
            choice = '5'
            shape_calc.view_history

        elif choice == '6' or choice == 'Exit':
            choice == '6'
            print("Exiting...")
            time.sleep(3)
            print("Have a nice day.")
            break

        else:
            print("Invalid input. Please try again")

if __name__ == '__main__':
    main_menu()