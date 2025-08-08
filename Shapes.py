import turtle


class Shapes:
    import turtle

    def __init__(self, x_axis, y_axis, color, size):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.color = color
        self.size = size

    screen = turtle.Screen()
    screen.title("Your turtle shapes")
    turtle.shape("turtle")
    pen = turtle.Turtle()
    pen.speed(0)

