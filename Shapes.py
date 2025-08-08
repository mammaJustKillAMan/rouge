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




    screen = turtle.Screen()
    screen.title("Your turtle shapes")
    turtle.shape("turtle")
    pen = turtle.Turtle()
    pen.speed(0)

