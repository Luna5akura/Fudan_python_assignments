def main():

    print("今有一个数，")
    try:
        x = int(input("若用 3 除余数为:"))
        y = int(input("若用 5 除余数为:"))
        z = int(input("若用 7 除余数为:"))
    except ValueError:
        print("输入错误")
        exit()

    s = [i for i in range(1000) if (i% 3 == x and i % 5 == y and i % 7 == z)  ]
    print("在0~1000中有这样的数:",s)


if __name__ == '__main__':
    main()