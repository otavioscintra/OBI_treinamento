def main():
    d = int(input())
    a = int(input())
    n = int(input())

    valor_diaria = d + (n - 1) * a if n <= 15 else d + 14 * a
    preco = valor_diaria * (32 - n)

    print(preco)


if __name__ == "__main__":
    main()
