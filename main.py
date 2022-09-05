from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(800, 600)
    screen.title("Breakout game")

    paddle = Paddle(position=(0, -250))
    ball = Ball()

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

        # detect the collision with wall
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        # detect collision with paddle
        if ball.distance(paddle) < 20 and ball.xcor() > -320:
            ball.bounce_y()

    screen.exitonclick()


if __name__ == "__main__":
    main()
