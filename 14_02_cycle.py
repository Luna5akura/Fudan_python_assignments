def right_shift(orgList, times):
    return orgList[-times:] + orgList[0:-times]


test = [1, 2, 3, 4, 5, 6, 7]

if __name__ == '__main__':
    print(right_shift(test, 3))
