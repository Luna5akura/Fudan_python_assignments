import turtle

turtle.colormode(255)
colors = ['red', 'orangered', 'orange',
          (253, 198, 11), 'yellow', 'yellowgreen',
          'green', (6, 150, 187), 'blue',
          (68, 78, 153), 'purple', (196, 3, 125)]
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def draw_square(pen_color, fill_color, size, start_x, start_y):
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.color(pen_color, fill_color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()


def main():
    screen = turtle.Screen()
    screen.setup(800, 200)
    screen.title('color_squares')
    screen.bgcolor('white')
    for i in range(len(colors)):
        draw_square(colors[i], colors[i], 50, -355 + 60 * i, -20)
    screen.mainloop()


if __name__ == '__main__':
    main()
