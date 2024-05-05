def bin_oct_hex():
    try:
        x = int(input("请输入十进制整数："))
    except ValueError:
        print("输入错误。")
        exit()
    b = bin(x)
    o = oct(x)
    h = hex(x)
    str1 = "二进制："
    str2 = "八进制："
    str3 = "十六进制："
    print(f"{str1:>{10 - len(str1)}} {b}")
    print(f"{str2:>{10 - len(str2)}} {o}")
    print(f"{str3:>{10 - len(str3)}} {h}")


if __name__ == "__main__":
    bin_oct_hex()
