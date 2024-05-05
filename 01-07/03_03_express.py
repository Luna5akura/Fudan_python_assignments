def express(weight, code):
    cost_map = [None,(13, 3), (12, 2), (14, 4)]
    base_cost, additional_cost = cost_map.__getitem__(code)
    cost = base_cost + max(weight - 2, 0) * additional_cost
    print(f"快递费为 {cost} 元")
    return


def main():
    try:
        w = float(input("请输入快递重量："))
        print("地区编号：\n1：华东地区\n2：华南地区\n3：华北地区")
        c = int(input("请输入地区编号："))

        if c not in [1, 2, 3]:
            print("输入错误！")
            return
        express(w, c)
        return

    except ValueError:
        print("输入错误！")
        return


if __name__ == "__main__":
    main()
