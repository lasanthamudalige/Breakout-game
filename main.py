from turtle import Screen
from paddle import Paddle


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(800, 600)
    screen.title("Breakout game")

    paddle = Paddle(position=(0, -250))

    # Move left and right when user press left/right arrow keys or a,d keys on the keyboard
    screen.listen()
    screen.onkey(paddle.go_left, "a")
    screen.onkey(paddle.go_right, "d")
    screen.onkey(paddle.go_left, "Left")
    screen.onkey(paddle.go_right, "Right")

    screen.exitonclick()


if __name__ == "__main__":
    main()
