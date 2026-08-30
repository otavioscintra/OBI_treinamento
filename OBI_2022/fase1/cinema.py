def main():
    i_1 = int(input())
    i_2 = int(input())
    preco = 0

    if i_1 < 18:
        preco += 15
    elif i_1 < 60:
        preco += 30
    else:
        preco += 20

    if i_2 < 18:
        preco += 15
    elif i_2 < 60:
        preco += 30
    else:
        preco += 20

    print(preco)


if __name__ == "__main__":
    main()
