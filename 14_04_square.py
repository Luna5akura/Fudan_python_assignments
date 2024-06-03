def square_number(n):
    sqr = set()
    nmb = 1
    cnt = 0
    while cnt < n:
        if nmb * nmb - 168 not in sqr or nmb * nmb < 268:
            sqr.add(nmb * nmb)
        else:
            cnt += 1
            yield nmb * nmb - 268
        nmb += 1


if __name__ == '__main__':
    for i in square_number(3):
        print(i)
