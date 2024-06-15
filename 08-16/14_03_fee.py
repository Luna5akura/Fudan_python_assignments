def cost(s, v):
    t = s / v
    a = 1.5 if t <= 15 else 1.5 + ((t - 15) // 15 + 1) * 1.5
    b = 1.5 if t <= 30 else 1.5 + ((t - 30) // 15 + 1) * 1
    c = 1.5 if t <= 15 else 1.5 + ((t - 15) // 10 + 1) * 1
    # find the minimum choice
    result = {'a': a, 'b': b, 'c': c}
    min_choice = min(result, key=result.get)
    print(f"The minimum cost is {result[min_choice]},chose {min_choice}")


if __name__ == '__main__':
    cost(600, 10)
