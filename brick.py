from turtle import Turtle


class Brick(Turtle):

    def __init__(self, position, color):
        super(Brick, self).__init__(shape="square")
        self.color(color)
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)
        self.tilt(90)