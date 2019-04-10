from functools import wraps


def add_chars(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return "<<< " + f(*args, **kwargs) + " >>>"
    return wrapper


@add_chars
def gen_message(greeting, name):
    return greeting + ", " + name + "!"


def main():
    msg = gen_message("Yo", "Bob")
    print(gen_message.__name__)


if __name__ == '__main__':
    main()
