def main(list1, list2):
    try:
        dict1 = {}
        for i in list1:
            dict1[i] = dict1.get(i, 0) + 1

        result = []
        for i in list2:
            if i in dict1 and dict1[i] > 0:
                result.append(i)
                dict1[i] -= 1

        return result
    except Exception as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":
    lst1 = [1, 2, 2, 3, 4]
    lst2 = [2, 2, 2, 4, 5]
    rtn = main(lst1, lst2)
    print(f"{lst1=}\n{lst2=}\n{rtn=}")
