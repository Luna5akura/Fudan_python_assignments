def main(list1, list2):
    try:
        if len(list1) > len(list2):
            return False
        for i in list1:
            if i in list2:
                list2.pop(list2.index(i))
            else:
                return False
        return True
    except Exception as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":
    test1 = [1, 2, 4, "b"]
    test2 = [1, 2, 3, 4, 5, "a", "b"]
    rtn = main(test1, test2)
    print(f"{rtn=}")
