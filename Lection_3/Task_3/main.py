def drawRhombus(default=28, size=29):
    print(' ' * int(default / 2), end='')
    print('*' * (size - default), end='')
    print(' ', end='\n')
    if default != 0:
        drawRhombus(default-2, size)
        print(' ' * int(default / 2), end='')
        print('*' * (size - default), end='')
        print(' ', end='\n')


def main():
    size = int(input("Size >>_"))
    if size % 2 == 0:
        size += 1
    drawRhombus(size-1, size)


if __name__ == '__main__':
    main()
