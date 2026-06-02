def main():
    N = 5
    alturas = [200, 180, 190, 140, 160]
    nao_vistos = 0
    maior_altura_vista = alturas[-1]

    for i in range(N - 2, -1, -1):
        if alturas[i] <= maior_altura_vista:
            nao_vistos += 1
        else:
            maior_altura_vista = alturas[i]

    print(nao_vistos)


if __name__ == "__main__":
    main()
