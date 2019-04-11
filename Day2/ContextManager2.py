from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    # Consider this to be the __enter__
    print("Opening the file")
    the_file = open(filename, mode)
    yield the_file

    # Consider this to be __exit__
    print("\nClosing the file")
    the_file.close()


def main():
    with open_file("input.txt", "r") as infile:
        for line in infile:
            print(line, end="")


if __name__ == '__main__':
    main()
