class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file")
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("\nClosing file")
        self.open_file.close()


def main():
    with File("input.txt", "r") as infile:
        for line in infile:
            print(line, end="")


if __name__ == '__main__':
    main()
