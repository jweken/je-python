import unicodedata


def random_example():
    '''A pseudo-random sequence 
       of Unicode characters\n
       See also: https://unicode-table.com/en/

       '''
    print('\nA few named Unicode characters:\n')
    lcb = unicodedata.lookup('LEFT CURLY BRACKET')  # "\N{AMPERSAND}"
    atts = unicodedata.lookup('ADDRESSED TO THE SUBJECT')
    solidus = unicodedata.lookup('solidus')
    uexcl = "\N{percent sign}"
    boxhl = "\N{box drawings light horizontal}"
    macron = "\N{macron}"
    revmac = unicodedata.lookup('airplane')
    line = boxhl*80
    print(line)
    print(solidus, atts, lcb, uexcl, macron, revmac,
          boxhl, '\u25b7', '\u2654', '\u265A')
    print(line)


if __name__ == '__main__':
    random_example()
