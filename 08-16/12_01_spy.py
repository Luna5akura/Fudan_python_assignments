import re

pattern = re.compile(r'特工.{3}')
sample = '特工张大三让特工李小四把图纸 USB 交给特工王二麻。'


def replace_name(match):
    matched_string = match.group()
    print(matched_string)
    return matched_string[2] + "**"


def main():
    replaced_sample = pattern.sub(replace_name, sample)
    print(replaced_sample)


if __name__ == '__main__':
    main()
