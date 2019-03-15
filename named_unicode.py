import unicodedata


def random_example():
    print('Some named Unicode characters:\n')
    uamp = "\N{AMPERSAND}"
    uexcl = "\N{percent sign}"
    boxhl = "\N{box drawings light horizontal}"
    macron = "\N{macron}"
    line = boxhl*8
    print(uamp, uexcl, macron, boxhl, line, '\u25b9')


if __name__ == '__main__':
    random_example()
