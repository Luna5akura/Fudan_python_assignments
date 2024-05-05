import re


def counter(given_list: list = None) -> dict:
    if given_list is None:
        given_list = []
    dic = {}
    for element in given_list:
        dic[element] = dic.get(element, 0) + 1
    return dic


def extract_letters(s: str) -> str:
    return ''.join(re.findall(r'[a-zA-Z]+', s))


def main():
    inpt = input("输入一段英文：")
    letters = extract_letters(inpt)
    output = counter([i for i in letters.lower()])
    for key, value in output.items():
        print(f'{key}:{value}')


if __name__ == '__main__':
    main()


def ascii_list_counter(s) -> list:
    count_list = [0 for _ in range(26)]
    for char in s:
        count_list[ord(char) - ord("a")] += 1
    output = sorted(
        zip(
            [chr(ord("a") + i) for i in range(26)],
            count_list
        ),
        key=lambda x: -x[1]
    )
    return output


def main2():
    inpt = input("输入一段英文：")
    letters = extract_letters(inpt)
    output = ascii_list_counter(letters.lower())
    for key, value in output:
        if value == 0:
            break
        print(f'{key}:{value}')


if __name__ == '__main__':
    main2()
