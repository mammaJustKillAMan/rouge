import turtle


class Shapes:
    import turtle

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
        return math.sqrt(3 / 4) * pow(self.size)

class Rectangle(Shapes):
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
            self.pen.right(108)
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



screen = turtle.Screen()
screen.title("Your turtle shapes")
turtle.shape("turtle")

if __name__ == "__main__":
    shapes = Shapes()

    while True:
        print("\n--- DRAWING MENU ---")
        print("1. Circle")
        print("2. Triangle")
        print("3. Rectangle")
        print("4. Pentagon")
        print("5. Hexagon")
        print("6. Exit")

        choice = input("Enter your choice: ")
        x_axis = input("Enter starting point at x axis: ")
        y_axis = input("Enter starting point at y axis: ")
        color = input("Enter shape color: ")
        size = input("Enter size of shape: ")

        if choice == "1":
            Circle(x_axis, y_axis, color, size)
            shapes.draw()
        elif choice == "2":
            Triangle(x_axis, y_axis, color, size)
            shapes.draw()
        elif choice == "3":
            Rectangle(x_axis, y_axis, color, size)
            shapes.draw()
        elif choice == "4":
            Pentagon(x_axis, y_axis, color, size)
            shapes.draw()
        elif choice == "5":
            Hexagon(x_axis, y_axis, color, size)
            shapes.draw()
        elif choice == "6":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice!")