from collections import Counter


def main():
    text = "When I was a kid I always wanted a cat but all I got was a gold fish"
    count = Counter(text.split())
    for w, c in count.most_common(3):
        print(w, "=>", c)

    numbers = [1, 2, 1, 4, 2, 6, 6, 4, 2]
    count2 = Counter(numbers)
    print(count2)


if __name__ == '__main__':
    main()
