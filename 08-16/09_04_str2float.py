def str_to_float():
    numbers = ['3.14', '-9', '4', '-2', '1.61']
    converted_numbers = map(float, numbers)
    return list(converted_numbers)


def main():
    result = str_to_float()
    print(result)


if __name__ == '__main__':
    main()