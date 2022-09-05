from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__(shape="square")
        self.color("blue")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.tilt(90)
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())
