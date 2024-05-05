import random

total = 0
right = 0
threshold = 1e-100
print(threshold)

while True:
    x1 = random.choice(range(0, 11))
    x2 = random.choice(("+", "-", "*", "/"))
    x3 = random.choice(range(0, 11)) if x2 != "/" else random.choice(range(1, 11))

    print(f"{x1}{x2}{x3}=")

    ans = input()
    if ans == 'q':
        break

    total += 1
    result = eval(f"{x1}{x2}{x3}")

    try:
        print(abs(float(ans) - result))
        if ((type(result) == int or (type(result)== float and (result * 1000).is_integer())) and abs(float(ans) - result) < threshold)\
                or (type(result) == float and not (result * 1000).is_integer() and abs(float(ans) - result) < 0.01):
            print('right')
            right += 1
        else:
            print('wrong')
    except ValueError:
        print('wrong,invalid number')
        continue

print(f"total:{total},right:{right},accuracy:{right / total :.2f}")
