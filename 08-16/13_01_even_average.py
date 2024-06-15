def main(inpt: list) -> float:
    try:
        filtered = list(filter(lambda x: x % 2 == 0, inpt))
        return sum(filtered) / len(filtered)
    except Exception as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":
    test = [i for i in range(100)]
    rtn = main(test)
    print(f"{test=}\n{rtn=}")