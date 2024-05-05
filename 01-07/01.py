import math
import turtle


def calculate_square():
    try:
        r = float(input("Enter your radius"))
    except ValueError:
        print("Invalid input")
        exit()
    sqr = math.pi * r * r
    print("The square is:{:.2f}".format(sqr))


def fibonacci(a, b, limit):
    if b < limit:
        print(a, end=",")
        fibonacci(b, a + b, limit)
    else:
        print(a)
    return


# 感觉plt会更好用


def centered_circle():
    turtle.pensize(5)
    turtle.circle(100)
    turtle.circle(50)
    turtle.circle(25)
    turtle.done()


def colorful_circle():
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]

    for i in range(7):
        color = colors[i]
        turtle.color(color, color)
        turtle.begin_fill()
        if i % 2 ==1:
            turtle.end_fill()
            turtle.penup()
        turtle.right(360 / 7)
        turtle.circle(50)
        if i % 2 == 1:
            turtle.begin_fill()
            turtle.pendown()
        turtle.end_fill()
    turtle.done()


def star():
    turtle.color('red', 'red')
    turtle.begin_fill()

    for _ in range(5):
        turtle.forward(200)
        turtle.right(144)

    turtle.end_fill()
    turtle.done()


if __name__ == '__main__':
    calculate_square()
    fibonacci(0, 1, 1000)
    # centered_circle()

    colorful_circle()
    star()
