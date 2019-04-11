def gen_range(n):
    print("Starting generator")
    value = 0
    while value < n:
        yield value
        value += 1


def main():
    g = gen_range(10)

    for i in g:
        if i == 7:
            break

    print("We are out")
    print(next(g))


if __name__ == '__main__':
    main()
