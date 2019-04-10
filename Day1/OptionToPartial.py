def pow_factory(f, ex):
    def inner(b):
        return f(b, ex)
    return inner


def pow(base, exp):
    return base**exp


def main():
    square = pow_factory(pow, 2)
    cube = pow_factory(pow, 3)

    print(square(3))
    print(cube(3))


if __name__ == '__main__':
    main()
