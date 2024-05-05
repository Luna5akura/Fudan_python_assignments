def bmi(weight, height):
    return weight / ((height / 100) ** 2)


def main():
    try:
        h = float(input("请输入您的身高（cm）："))
        w = float(input("请输入您的体重（kg）："))

        b = bmi(w, h)
        print("您的BMI指数为：", b, end="，")

        if b < 18.5:
            print("您的体重过轻！")
        elif b < 25:
            print("您的体重正常！")
        elif b < 30:
            print("您的体重过重！")
        elif b < 35:
            print("您的体重为肥胖1级！")
        elif b < 40:
            print("您的体重为肥胖2级！")
        else:
            print("您的体重为肥胖3级！")
    except ValueError:
        print("输入有误！")


if __name__ == '__main__':
    main()
