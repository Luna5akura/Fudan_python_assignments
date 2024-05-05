def segment_func(x):
    if x < 0:
        return 0
    elif x < 5:
        return x
    elif x < 10:
        return 3 * x - 5
    elif x < 20:
        return x - 2
    return 0


def main():
    try:
        y = segment_func(int(input("Please enter x")))
    except ValueError:
        print("Invalid input")
        exit()

    print(f"The output is {y}")


if __name__ == "__main__":
    main()
