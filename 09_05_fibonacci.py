from functools import reduce


def fibonacci_sequence(n):
    initial = [(0, 1)]
    fib_n = lambda t, _: (t[1], t[0] + t[1])
    fib_numbers = reduce(lambda acc, _: acc + [fib_n(acc[-1], None)], range(n), initial)
    return list(map(lambda x: x[0], fib_numbers))


def main():
    n = 12
    print(fibonacci_sequence(n))


if __name__ == '__main__':
    main()
