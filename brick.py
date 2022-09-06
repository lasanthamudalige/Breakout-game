from turtle import Turtle
from time import sleep


class Bricks(Turtle):

    def __init__(self, position):
        super(Bricks, self).__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.tilt(90)

    # def show_colors(self):
    #     colors = ["red", "lime", "blue", "yellow", "cyan", "magenta", "silver", "grey", "maroon", "olive",
    #               "green", "purple", "teal", "navy", "coral", "salmon", "gold", "khaki", "olive", "green", "teal",
    #               "aqua", "turquoise", "navy", "indigo", "purple", "thistle", "plum", "violet", "orchid", "pink",
    #               "beige", "wheat", "sienna", "peru", "tan", "moccasin", "linen", "sea shell", "mint cream",
    #               "slate gray", "lavender", "floral white", "alice blue", "ghost white", "honeydew", "ivory", "azure",
    #               "snow"]
    #     for color in colors:
    #         x = -280
    #         y = 220
    #         Bricks((x, y))
    #         x -= 5
    #         sleep(1)
