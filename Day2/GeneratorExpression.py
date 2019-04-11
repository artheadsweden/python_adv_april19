def gen():
    my_numbers = [1, 2, 3, 4, 5]
    for value in my_numbers:
        yield value**2


def main():
    for i in gen():
        print(i)

    g = (value**2 for value in [1, 2, 3, 4, 5])
    for i in g:
        print(i)


if __name__ == '__main__':
    main()
