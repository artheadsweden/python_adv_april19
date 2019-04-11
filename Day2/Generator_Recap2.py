def gen_range(n):
    print("Starting generator")
    value = 0
    while value < n:
        yield value
        value += 1


def main():
    g = gen_range(3)
    print(next(g))
    print(next(g))
    g1 = gen_range(4)
    print(next(g1))
    print(next(g))



if __name__ == '__main__':
    main()
