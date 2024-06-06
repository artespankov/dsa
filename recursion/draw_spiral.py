import turtle

leo = turtle.Turtle()
screen = turtle.Screen()


def draw_spiral(line: int):
    if line:
        turtle.forward(line)
        turtle.right(90)
        draw_spiral(line-5)


if __name__ == "__main__":
    draw_spiral(100)
    screen.exitonclick()




