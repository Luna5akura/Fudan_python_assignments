# 太丑陋了

def anagram(lst, result=[]):
    if not lst:
        return result
    target = lst.pop()
    ana = list(filter(lambda x: sorted(x) == sorted(target), lst))
    ana.append(target)
    lst = [i for i in lst if i not in ana]
    result.append(ana)
    return anagram(lst, result)


def main():
    lst = ["eat", "tea", "tan", "ate", "nat", "bat"]

    result = anagram(lst)
    print(f"原始：{lst}")
    print(f"重新排列：{result}")


if __name__ == '__main__':
    main()
