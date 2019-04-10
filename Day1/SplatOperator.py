def func(*args, **kwargs):
    pass


def my_func(a, b, c):
    print(a, b, c)


def main():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_list = [10, 20, 30]

    my_func(my_list[0], my_list[1], my_list[2])
    my_func(*my_list)
    my_func(*my_dict)
    my_func(**my_dict)

    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    a, *b, c = my_tuple

    print(a, b, c)

    first, *_, last = my_tuple
    print(first, last)

    first = my_tuple[0]
    last = my_tuple[-1]
    print(first, last)




if __name__ == '__main__':
    main()
