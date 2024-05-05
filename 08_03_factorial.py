def factorial(n: int, simple=True, cache=None):
    if simple:
        return 1 if n < 2 else n * factorial(n - 1)
    if n < 1:
        return None
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 1:
        cache[n] = 1
        return 1
    cache[n] = n * factorial(n - 1, False, cache)
    return cache[n]


def sum_factorial(n: int, cache=None):
    if n < 1:
        return None
    if cache is None:
        cache = {}
    if n == 1:
        return factorial(1, False, cache)
    return factorial(n, False, cache) + sum_factorial(n - 1, cache)


if __name__ == '__main__':
    try:
        inpt = int(input('Enter a POSITIVE integer(less than 10):'))
    except ValueError:
        print("Invalid Input")
        exit()
    raw_output = "".join([f"{i}!+" for i in range(1, inpt + 1)])
    raw_output = raw_output[:-1] + "="

    print(raw_output + f"{sum_factorial(inpt)}")
