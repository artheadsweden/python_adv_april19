def add_chars(f):
    def wrapper(*args, **kwargs):
        return "<<< " + f(*args, **kwargs) + " >>>"
    return wrapper


@add_chars
def gen_message(greeting, name):
    return greeting + ", " + name + "!"


def call_gen_message():
    return gen_message("Hi", "Anna")


def main():
    #global gen_message
    #gen_message = add_chars(gen_message)
    msg = gen_message("Yo", "Bob")
    print(msg)
    print(call_gen_message())


if __name__ == '__main__':
    main()
