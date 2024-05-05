import random

def main():
    while True:
        try:
            n = int(input("输入正整数 n :"))
            li = [random.randint(0, 99) for _ in range(n)]
            print("初始的：",li)
            print("交换的：",li[::-1])
        except ValueError:
            print("输入错误，请输入正整数。")
            exit()


if __name__ == '__main__':
    main()