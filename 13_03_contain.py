def main(list1, list2):
    if len(list1) > len(list2):
        return False
    for i in list1:
        if i in list2:
            list2.pop(list2.index(i))
        else:
            return False
    return True

if __name__ == "__main__":
    list1 = [1, 2, 4, "b"]
    list2 = [1, 2, 3, 4, 5, "a", "b"]
    rtn = main(list1, list2)
    print(f"{rtn=}")
