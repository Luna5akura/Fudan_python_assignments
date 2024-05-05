dic = {(i + 3) % 10: i for i in range(10)}
str1 = "请输入外圈的数字0~9："


def outer():
    try:
        ans = dic[int(input(f"{str1:<12}"))]
    except ValueError:
        print(f"输入错误。")
        exit()
    print(f'对应的内圈数字0~9是：{ans:<12}')


if __name__ == '__main__':
    outer()
