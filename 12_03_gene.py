import re

pattern = re.compile("^ATG.*?(TAA|TAG|TGA)$")
invalid = re.compile("TAG|TAA|TGA")


def is_gene(inpt):
    if len(inpt) % 3:
        return False
    if len(inpt) < 6 or not pattern.search(inpt):
        return False
    for i in range(0, len(inpt) - 6, 3):
        codon = inpt[i + 3:i + 6]
        if invalid.match(codon):
            return False
    return True


def main():
    with open("gene.txt", "r") as file:
        f = file.readlines()
    output = []
    for line in f:
        line = line.strip()
        if is_gene(line):
            output.append(line)
    for index, gene in enumerate(output):
        print(f"{index + 1}:{gene}")


if __name__ == '__main__':
    main()
