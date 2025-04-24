import turtle
import math

def draw_equilateral_triangle(pen: turtle.Pen, side_length: float | int, angle: float | int = 90,
                              centered: bool = False, line_color: str = 'black', fill: bool = False,
                              fill_color: str = 'black', line_width: float | int = 1, hide_pen: bool = True) -> None:
    # Setup pen
    pen.pu()
    pen.color(line_color)
    pen.width(line_width)
    if hide_pen:
        pen.hideturtle()

    # Centering logic
    if centered:
        # Calculate the height of the equilateral triangle, also divide by 3 instead of 2 for center of triangle not line
        height = (math.sqrt(3) / 3) * side_length

        # Adjust pen position based on angle
        pen.setheading(angle)
        pen.backward(side_length / 2)
        pen.right(90)
        pen.forward(height / 2)
        pen.setheading(angle)
    pen.pd()

    if fill:
        pen.fillcolor(fill_color)
        pen.begin_fill()
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)  # Turn to form an equilateral triangle
    if fill:
        pen.end_fill()
    pen.pu()
