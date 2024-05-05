def main():
    score = []
    while True:
        payload = input("请输入一个成绩（直接输入回车退出）:")
        if not payload:
            break
        try:
            score.append(float(payload))
        except ValueError:
            print("输入错误，请输入数字")
    print(f"总共输入 {len(score)} 个成绩，")
    score.sort(reverse=True)
    print("最高分:", score[0])
    print("最低分:", score[-1])
    print("平均分:", sum(score) / len(score))
    print("中位数:", score[int(len(score) / 2)] if len(score) % 2 == 1 else (score[int(len(score) / 2 - 1)] + score[int(len(score) / 2)]) / 2)


if __name__ == '__main__':
    main()