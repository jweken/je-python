def content():
    x = ("Running", __file__)
    return str(x)


if __name__ == '__main__':
    print(content())
