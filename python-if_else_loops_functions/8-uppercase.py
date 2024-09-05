def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print("{:c}".format(ord(char)), end="")
    print()

uppercase("holberton")
uppercase("Holberton School")
uppercase("Holberton School, 98 battery street")
uppercase("")
uppercase("98")
uppercase("z")