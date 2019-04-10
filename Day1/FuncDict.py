def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def main():
    calc = {
        "add": lambda a, b: a + b,
        "subtract": sub,
        "multiply": mul,
        "divide": div,
    }

    print(calc["add"](2, 3))
    print(calc["subtract"](2, 3))
    print(calc["multiply"](2, 3))
    print(calc["divide"](2, 3))

    for k, f in calc.items():
        print(k, "=", f(2, 3))



if __name__ == '__main__':
    main()
