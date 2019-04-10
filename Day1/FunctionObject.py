def function_object(n=0):
    private_value = n

    def func():
        print("private_value =", private_value)

    def increase_by(x):
        nonlocal private_value
        private_value += x

    def decrease_by(x):
        nonlocal private_value
        private_value -= x

    def get_value():
        return private_value

    def set_value(new_value):
        nonlocal private_value
        private_value = new_value

    func.increase_by = increase_by
    func.decrease_by = decrease_by
    func.get_value = get_value
    func.set_value = set_value

    return func


def main():
    fo = function_object(10)
    fo2 = function_object(100)
    fo2.increase_by(50)
    fo.increase_by(2)
    fo()
    print(fo.get_value())
    fo.set_value(3)
    print(fo.get_value())
    print(fo2.get_value())



if __name__ == '__main__':
    main()
