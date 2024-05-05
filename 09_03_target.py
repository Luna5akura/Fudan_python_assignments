def two_sum(nums, target):
    hashmap = {}
    result = []
    for i, num in enumerate(nums):
        if target - num in hashmap:
            result.append((hashmap[target - num], i))
        hashmap[num] = i

    filtered_result = filter(lambda x: True, result)
    return list(filtered_result)


def main():
    nums = [2, 7, 7, 15]
    target = 9
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()
