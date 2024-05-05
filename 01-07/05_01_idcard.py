import re

pattern = r"^([1-6][1-9]|50)\d{4}(18|19|20)\d{2}((0[1-9])|10|11|12)(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$"


def main():
    idcard = input("请输入您的身份证号码：")
    if not re.match(pattern, idcard):
        print('输入的身份证号码格式不正确！')
        exit()
    else:
        print(f"您是{idcard[6:10]}年{int(idcard[10:12])}月{int(idcard[12:14])}日出生的。")
        print(f"您的性别是：{'男' if int(idcard[16]) % 2 == 1 else '女'}。")
        print(f"您的身份证校验码是：{idcard[-1]}")


if __name__ == '__main__':
    main()
