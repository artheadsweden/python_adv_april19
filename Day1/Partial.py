from functools import partial


def pow(base, exp):
    return base**exp


def main():
    result = pow(3, 2)
    print(result)
    square = partial(pow, exp=2)
    cube = partial(pow, exp=3)
    print(square(3))
    print(cube(3))



if __name__ == '__main__':
    main()
