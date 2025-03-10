huge_num = {
    '0': '000000   00   00   00   00   000000',
    '1': '  1   11  1 1    1    1    1  11111',
    '2': '22222    2    2222222    2    22222',
    '3': '33333    3    333333    3    333333',
    '4': '   4   44  4 4 44444   4    4    4 ',
    '5': '555555    5    55555    5    555555',
    '6': '666666    6    666666   66   666666',
    '7': '77777    7    7   7   7   7   7    ',
    '8': '888888   88   8888888   88   888888',
    '9': '999999   99   999999    9    999999'
}


def huge():
    while True:
        payload = input("请输入一串数字")
        if not payload.isdigit():
            print('输入的不是一串有效数字！')
            continue
        output = [[huge_num[i][j:j + 5] + " " for i in payload] for j in range(0, 35, 5)]
        for i in output:
            print("".join(i))


if __name__ == '__main__':
    huge()
