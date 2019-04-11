def coroutine():
    print("Starting up")
    count = 0
    while True:
        data = yield
        print(data, count)
        count += 1


def main():
    co = coroutine()
    next(co)
    print("I'm back in main")
    co.send("Hi coroutine")
    print("I'm back in main")
    co.send("Hi coroutine")
    print("I'm back in main")
    co.send("Hi coroutine")
    print("I'm back in main")
    co.send("Hi coroutine")


if __name__ == '__main__':
    main()
