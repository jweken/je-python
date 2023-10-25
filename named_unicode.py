import unicodedata


def random_example():
    '''A pseudo-random sequence 
       of Unicode characters\n
       See also: https://unicode-table.com/en/

    '''
    doc = __file__
    print(f'\nA few named Unicode characters from {doc}:\n')
    lcb = unicodedata.lookup('LEFT CURLY BRACKET')
    atts = unicodedata.lookup('ADDRESSED TO THE SUBJECT')
    solidus = unicodedata.lookup('solidus')
    uexcl = "\N{percent sign}"
    boxhl = "\N{box drawings light horizontal}"
    macron = "\N{macron}"
    revmac = unicodedata.lookup('airplane')
    line = boxhl*80
    pawn = '\u2659'
    whitepawn = '\u265f'
    print(line)
    print(lcb, solidus, atts, lcb, uexcl, macron, revmac,
          boxhl, '\u25b7', '\u2654', '\u265A', pawn, whitepawn)
    print(line)


if __name__ == '__main__':
    random_example()
