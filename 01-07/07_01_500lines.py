import turtle


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("500lines")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    for length in range(1, 501):
        pen.forward(length)
        pen.right(91)

    screen.mainloop()


if __name__ == "__main__":
    main()
