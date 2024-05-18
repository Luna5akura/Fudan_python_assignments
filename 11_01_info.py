import csv

# PATH = './_11_01_填报选项.txt'
PATH = './填报选项.txt'


def main():
    with open(PATH, 'r', encoding='utf-8') as f:
        options = [line.strip() for line in f]

    info = {}
    for option in options:
        if "：" not in option:
            info[option] = input(f'请输入{option}: ')
        else:
            question, option = option.split("：")
            info[question] = input(question + "".join(
                ["\n" + str(index) + " -- " + option for index, option in enumerate(option.split("、"))]))

    with open('填报信息.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(info.keys())
        writer.writerow(info.values())

    print('填报信息已保存到 填报信息.csv 文件中。')


if __name__ == '__main__':
    main()
