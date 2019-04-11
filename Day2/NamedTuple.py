from collections import namedtuple


def main():
    Student = namedtuple('Student', ['name', 'age', 'email'])
    s = Student("John", email='john65@email.com', age='19')
    print(s.name)
    print(s.age)
    print(s[1])


if __name__ == '__main__':
    main()
