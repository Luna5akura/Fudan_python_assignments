# "Rose is a rose is a rose is a rose." written by Gertrude Stein

def main():
    char = input("请输入一段英文：")

    if max(ord(i) for i in char) > 127:
        print("警告：输入的字符串非纯英文")
    output = "".join([chr(ord(i) - 32) if 97 <= ord(i) <= 122 else (chr(ord(i) + 32) if 65 <= ord(i) <= 90 else i) for i in char])
    print(output)


if __name__ == '__main__':
    main()


def main2():
    char = input("请输入一段英文：")
    print(str.__getattribute__(char, "swapcase")())


# main2()


class StringEx(str):
    def backup_swapcase(self):
        """
        Swaps cases in a copy of the string.
        """
        b = super().__new__(self.__class__, self) # class  self.deepcopy()
        b = "".join([i.upper() if 97 <= ord(i) <= 122 else (i.lower() if 65 <= ord(i) <= 90 else i) for i in b])
        return b


def main3():
    char = StringEx(input("请输入一段英文："))
    print(char.backup_swapcase())


# main3()
