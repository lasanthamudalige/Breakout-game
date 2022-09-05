from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("grey")
        self.penup()