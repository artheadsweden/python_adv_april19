from dataclasses import *

@dataclass
class Person:
    name: str
    age: int
    email: str

    def birthday(self):
        self.age += 1


def main():
    p1 = Person("Peter", 34, "peter@mail.com")
    print(p1)
    p1.birthday()
    print(p1)
    print(p1.name)


if __name__ == '__main__':
    main()
