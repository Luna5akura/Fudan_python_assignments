# def main():
#     with open("sleepy.in", "r") as f:
#         length = int(f.readline())
#         lst = [int(i) for i in f.readline().split()]
#     target = [i + 1 for i in range(length)]
#     cnt = 0
#     while lst != target:
#         cnt += 1
#         current = lst[0]
#         smaller = filter(lambda x: x < current, lst)
#         idxs = [smaller.index(i) for i in smaller]
#         idx = max(idxs)
#         lst = lst[1:idx + 1] + [current] + lst[idx + 1:]
#     with open("sleepy.out", "w") as f:
#         f.write(str(cnt))

def main():
    with open("sleepy.in", "r") as f:
        length = int(f.readline())
        lst = [int(i) for i in f.readline().split()]

    sorted_num = 1
    for i in range(length - 2, -1, -1):
        if lst[i] < lst[i + 1]:
            sorted_num += 1
        else:
            break

    result = length - sorted_num

    with open("sleepy.out", "w") as f:
        f.write(f"{result}\n")


if __name__ == "__main__":
    main()
