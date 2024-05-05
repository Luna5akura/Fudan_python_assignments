import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.penup()
pen.goto(-300, -70)
pen.pendown()
pen.hideturtle()


def koch(size, layer):
    if layer == 0:
        pen.forward(size / 3)
    else:
        for angle in [0, 60, -120, 60]:
            pen.left(angle)
            koch(size / 3, layer - 1)


def main():
    screen = turtle.Screen()
    screen.setup(800, 400)
    screen.title('科赫曲线')
    screen.bgcolor("white")
    layer = 3
    size = 600 * 3
    koch(size, layer)
    screen.mainloop()


if __name__ == '__main__':
    main()
