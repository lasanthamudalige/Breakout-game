import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
import time


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(800, 600)
    screen.title("Breakout game")
    screen.tracer(0)

    paddle = Paddle(position=(0, -250))
    ball = Ball()

    bricks = 0
    x = -360
    y = 220
    for i in range(45):
        colors = ["red", "lime", "blue", "yellow", "cyan", "magenta", "silver", "grey", "maroon", "olive",
                  "green", "purple", "teal", "navy", "coral", "salmon", "gold", "khaki", "olive", "green", "teal",
                  "aqua", "turquoise", "navy", "indigo", "purple", "thistle", "plum", "violet", "orchid", "pink",
                  "beige", "wheat", "sienna", "peru", "tan", "moccasin", "linen", "mint cream",
                  "slate gray", "lavender", "floral white", "alice blue", "ghost white", "honeydew", "ivory", "azure",
                  "snow"]
        random_color = random.choice(colors)
        Brick((x, y), random_color)
        x += 90
        bricks += 1

        if bricks % 9 == 0:
            x = -360
            y -= 30


    # Move left and right when user press left/right arrow keys or a,d keys on the keyboard
    screen.listen()
    screen.onkey(paddle.go_left, "a")
    screen.onkey(paddle.go_right, "d")
    screen.onkey(paddle.go_left, "Left")
    screen.onkey(paddle.go_right, "Right")

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # detect the collision with left and right wall
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        # detect collision with paddle
        if ball.distance(paddle) < 35 and ball.xcor() > -320:
            ball.bounce_y()

        # detect collision with top wall
        if ball.ycor() > 280:
            ball.bounce_y()

        # if ball.distance()

    screen.exitonclick()


if __name__ == "__main__":
    main()
