def solver():
    list1 = [(i, 100 - 5 * i) for i in range(round(100 / 5))]
    solutions = [(a, b, 100 - a - b) for a, money in list1 for b in range(money + 1) if
                 (money - 3 * b) * 3 + a + b == 100]
    for i in solutions:
        print(i)


if __name__ == '__main__':
    solver()
