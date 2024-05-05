import operator

operate_dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def calc():
    input1 = (input("请输入第一个数字:"))
    try:
        input1 = float(input1)
    except ValueError:
        print("数字输入错误。")
        return

    calc_symbol = input("运算符(+ - * /):")
    if calc_symbol not in operate_dict:
        print("无效的运算符。")
        return

    input2 = (input("请输入第二个数字:"))
    try:
        input2 = float(input2)
    except ValueError:
        print("数字输入错误。")
        return

    try:
        ans = operate_dict[calc_symbol](input1, input2)
    except ZeroDivisionError:
        print("除数不能为0。")
        return

    print(f"运算结果：{ans}")


if __name__ == '__main__':
    calc()
