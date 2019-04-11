def genco():
    data = "Empty"
    while True:
        data += yield data


def main():
    gc = genco()
    print(next(gc))
    print(gc.send("Oh"))
    print(gc.send("Ok"))
    print(gc.send("Yes"))


if __name__ == '__main__':
    main()
