def pivot(dic: dict):
    rtn = {}
    for key, value in dic.items():
        for v in value:
            if v not in rtn:
                rtn[v] = set()
            rtn[v].add(key)
    return rtn


test = {'a': {1, 2, 3}, "b": {1, 2}, "c": {2, 3}, "d": {3, 4}}

if __name__ == '__main__':
    print(pivot(test))
