def main():
    data = "0983409382349876234078239847239873298743298723987987324987"
    price = data[13:16]
    amount = data[21:23]

    print(price, amount)

    PRICE = slice(13, 16)
    AMOUNT = slice(21, 23)

    price = data[PRICE]
    amount = data[AMOUNT]

    print(price, amount)



if __name__ == '__main__':
    main()
