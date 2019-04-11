def genco(data):
    #data = "Hi there"
    while True:
        f = yield
        f(data)


def main():
    gc = genco("Yes this works too")
    # Start the generator
    next(gc)

    # Send stuff to the generator
    gc.send(lambda value: print(value[::-1]))
    gc.send(lambda value: print(value))


if __name__ == '__main__':
    main()
