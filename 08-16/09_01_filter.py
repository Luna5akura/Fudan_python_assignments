def filter_max_negative(numbers):
    filt = filter(lambda x: x < 0, numbers)
    return max(filt)

def filter_min_positive(numbers):
    filt = filter(lambda x: x > 0, numbers)
    return min(filt)



def main():
    numbers = [-1, -2, -3, 4, 5, 6]

    print(f"原始数据：{numbers}")
    print(f"负数中的最大值：{filter_max_negative(numbers)}")
    print(f"正数中的最小值：{filter_min_positive(numbers)}")

if __name__ == '__main__':
    main()