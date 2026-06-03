def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)


def main():
    p = list(map(int, input().split()))
    n = list(map(int, input().split()))

    n_ord = quicksort(n)
    print(n_ord[-p[1]])


if __name__ == '__main__':
    main()
