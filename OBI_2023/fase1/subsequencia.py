def main():
    elem = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    inicio_busca = 0
    for i in b:
        try:
            pos = a.index(i, inicio_busca)
            inicio_busca = pos + 1
        except ValueError:
            print('N')
            return
    print("S")


if __name__ == "__main__":
    main()
