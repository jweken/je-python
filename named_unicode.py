import unicodedata


def random_example():
    '''A pseudo-random sequence 
       of Unicode characters'''
    print('\n\tSome named Unicode characters:\n')
    uamp = "\N{AMPERSAND}"
    uexcl = "\N{percent sign}"
    boxhl = "\N{box drawings light horizontal}"
    macron = "\N{macron}"
    line = boxhl*80
    print(line)
    print(uamp, uexcl, macron, boxhl, '\u25b7', '\u2654', '\u265A')
    print(line)


if __name__ == '__main__':
    random_example()
