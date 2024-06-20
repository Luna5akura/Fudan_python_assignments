def main(inpt):
    try:
        result = [1 if i > 90 else 0 for i in inpt ]
        return sum(result)
    except Exception as e:
        print(f"Error: {e}")
        exit()


if __name__ == '__main__':
    test = [i for i in range(100)]
    rtn = main(test)
    print(f"{rtn=}")
