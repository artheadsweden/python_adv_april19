from functools import wraps


def print_with_start(original_print):
    @wraps(original_print)
    def wrapper(*args, **kwargs):
        pre = ""
        if "start" in kwargs:
            pre = kwargs['start']
            kwargs.pop('start')
        original_print(pre, *args, **kwargs)

    return wrapper


print = print_with_start(print)


def main():
    x = 10
    print("x is", x)
    print("x", end="")
    print(x, start=" =")
    print(f"x is {x}", start="<", end=">\n", sep="")


if __name__ == '__main__':
    main()
