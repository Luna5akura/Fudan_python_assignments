def check_caps(text: str):
    pas = True
    itr = iter(enumerate(text))
    rtn = ""
    for idx, char in itr:
        rtn += char
        if char != ".":
            continue
        if idx == len(text) - 1:
            break
        while True:
            idx, char = itr.__next__()
            if char.isalpha() and char.islower():
                pas = False
                rtn += char.upper()
                break
            elif char.isupper():
                rtn += char
                break
            else:
                rtn += char
    print(f"Integrity: {pas}, Text: {rtn}")


test = ". Hello. world."

if __name__ == '__main__':
    check_caps(test)
