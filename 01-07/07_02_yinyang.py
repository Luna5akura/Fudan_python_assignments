import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def draw_half_circle(radius, rotate, start_x, start_y, pen_color='black', fill_color=None):
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.color(pen_color, fill_color)
    pen.begin_fill()
    pen.left(rotate)
    pen.circle(radius, 180)
    pen.left(90)
    pen.forward(2 * radius)
    pen.end_fill()
    pen.left(90 - rotate)


def draw_circle(radius, start_x, start_y, pen_color='black', fill_color=None):
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.color(pen_color, fill_color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def draw_yinyang():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("yinyang")
    screen.bgcolor("white")
    draw_half_circle(100, 0, 0, 0, fill_color='black')
    draw_half_circle(100, 180, 0, 200, fill_color='white')
    draw_circle(50, 0, 0, fill_color='black')
    draw_circle(50, 0, 100, pen_color='white', fill_color='white')
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color('black')
    pen.circle(100)
    screen.mainloop()


if __name__ == "__main__":
    draw_yinyang()
