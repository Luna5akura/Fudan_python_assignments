import os


def main():
    if not os.path.exists('temp1'):
        os.mkdir('temp1')

    for i in range(1, 11):
        filename = f'{i}.txt'
        filepath = os.path.join('temp1', filename)
        with open(filepath, 'w') as file:
            file.write(str(i))

    for filename in os.listdir('temp1'):
        if filename.endswith('.txt'):
            old_filepath = os.path.join('temp1', filename)
            new_filename = f'{int(filename[:-4]):03d}.txt'
            new_filepath = os.path.join('temp1', new_filename)
            os.rename(old_filepath, new_filepath)


if __name__ == '__main__':
    main()
