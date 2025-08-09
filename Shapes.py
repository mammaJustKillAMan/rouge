import math
import turtle
import webbrowser


class Shapes:

    def __init__(self, x_axis, y_axis, color, size):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.color = color
        self.size = size

        self.pen = turtle.Turtle()
        self.pen.speed(5)

    def draw(self):
        pass

    def area(self):
        pass

class Circle(Shapes):
    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x_axis, self.y_axis)
        self.pen.color(self.color)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def area(self):
        return self.size ** 2 * math.pi

class Triangle(Shapes):
    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x_axis, self.y_axis)
        self.pen.color(self.color)
        self.pen.pendown()
        self.pen.begin_fill()
        for _ in range(3):
            self.pen.forward(self.size)
            self.pen.right(120)
        self.pen.end_fill()

    def area(self):
        return (math.sqrt(3) / 4) * (self.size ** 2)

class Square(Shapes):
    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x_axis, self.y_axis)
        self.pen.color(self.color)
        self.pen.pendown()
        self.pen.begin_fill()
        for _ in range(4):
            self.pen.forward(self.size)
            self.pen.right(90)
        self.pen.end_fill()

    def area(self):
        return self.size ** 2

class Pentagon(Shapes):
    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x_axis, self.y_axis)
        self.pen.color(self.color)
        self.pen.pendown()
        self.pen.begin_fill()
        for _ in range(5):
            self.pen.forward(self.size)
            self.pen.right(72)
        self.pen.end_fill()

    def area(self):
        return (self.size ** 2 * math.sqrt(25 + 10 * math.sqrt(5))) / 4

class Hexagon(Shapes):
    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x_axis, self.y_axis)
        self.pen.color(self.color)
        self.pen.pendown()
        self.pen.begin_fill()
        for _ in range(6):
            self.pen.forward(self.size)
            self.pen.right(60)
        self.pen.end_fill()

    def area(self):
        return (3 * math.sqrt(3) / 2) * (self.size ** 2)



def get_number(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print("Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_color(prompt):
    while True:
        try:
            color = input(prompt)
            turtle.Turtle().color(color)
            return color
        except ValueError:
            print("Invalid input. Please enter a color.")


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Your turtle shapes")
    turtle.shape("turtle")

    while True:
        print("\n--- DRAWING MENU ---")
        print("1. Circle")
        print("2. Triangle")
        print("3. Rectangle")
        print("4. Pentagon")
        print("5. Hexagon")
        print("6. Exit")
        print("7. Color manu")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("Thank you for playing!")
            break
        elif choice == "7":
            webbrowser.open("https://www.w3schools.com/colors/colors_names.asp")

        x_axis = get_number("Enter starting point at x axis: ", -400, 400)
        y_axis = get_number("Enter starting point at y axis: ", -300, 300)
        color = get_color("Enter shape color: ")
        size = get_number("Enter size of shape: ", 1, 400)

        if choice == "1":
            shape = Circle(x_axis, y_axis, color, size)
        elif choice == "2":
            shape = Triangle(x_axis, y_axis, color, size)
        elif choice == "3":
            shape = Square(x_axis, y_axis, color, size)
        elif choice == "4":
            shape = Pentagon(x_axis, y_axis, color, size)
        elif choice == "5":
            Hexagon(x_axis, y_axis, color, size)
            shapes.draw()
        elif choice == "6":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice!")