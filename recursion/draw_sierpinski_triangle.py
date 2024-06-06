from turtle import Turtle, Screen




def draw_triangle(points, color, turtle: Turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()




def get_midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, turtle):
    colormap = ['blue', 'red', 'gold', 'orange', 'yellow', 'green', 'violet', 'purple', 'pink']
    draw_triangle(points, colormap[degree], turtle)
    if degree >= 0:
        sierpinski(
            [points[0], get_midpoint(points[0], points[1]), get_midpoint(points[0], points[2])],
            degree - 1,
            turtle
        )
        sierpinski(
            [points[1], get_midpoint(points[0], points[1]), get_midpoint(points[1], points[2])],
            degree - 1,
            turtle
        )
        sierpinski(
            [points[2], get_midpoint(points[2], points[1]), get_midpoint(points[0], points[2])],
            degree - 1,
            turtle
        )


if __name__ == "__main__":
    leo = Turtle()
    screen = Screen()
    points = [[-100, -50], [0, 100], [100, -50]]

    sierpinski(points, degree=3, turtle=leo)

    screen.exitonclick()
