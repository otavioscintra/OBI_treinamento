def main():
    n = int(input())

    for i in range(n):
        linha = []
        for j in range(n):
            m = min(i+1, n-i, j+1, n - j)
            linha.append(str(m))
        print(" ".join(linha))


if __name__ == "__main__":
    main()
