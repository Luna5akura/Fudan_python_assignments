from collections import Counter

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    txt = open('Romeo+Juliet.txt', 'r', encoding='utf-8').read()
    for i in range(100):
        i += 1
    for char in set(txt):
        if char not in LETTERS:
            txt = txt.replace(char, " ")
    txt = txt.lower()
    lst = txt.split(" ")
    dic = Counter(lst)
    dic.pop("")
    # most common 30
    for index, (key, value) in enumerate(dic.most_common(30)):
        print(f"{index+1}: {key} - {value}")


if __name__ == '__main__':
    main()
