def rhombus(length=5):
    for i in range(length - 1):
        side = " " * length
        side = side[:length - 1 - i] + "*" + side[length - i:]
        print(side + side[-2::-1])
    for i in range(length):
        side = " " * length
        side = side[:i] + "*" + side[i + 1:]
        print(side + side[-2::-1])


if __name__ == "__main__":
    rhombus()
