# "Rose is a rose is a rose is a rose." written by Gertrude Stein

import re

pattern = r"\b[Rr]ose\b"


def main():
    char = input("请输入一段英文：")
    amounts = re.findall(pattern, char)

    print(f"总共有{len(amounts)}个玫瑰，出现的序号为：")

    for i in re.finditer(pattern, char):
        print(i.start())


if __name__ == "__main__":
    main()
