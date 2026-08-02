def main():
    n, m = map(int, input().split())
    b = []
    for i in range(n):
        b.append(list(map(int, input().split())))
    par_cor0 = 0
    impar_cor0 = 0
    par_cor1 = 0
    impar_cor1 = 0
    custo = 0
    cor0_deve_ser_par = False

    for i in range(n):
        for j in range(m):
            cor = (i+j) % 2

            if cor == 0:
                if b[i][j] % 2 == 0:
                    par_cor0 += 1
                else:
                    impar_cor0 += 1
            else:
                if b[i][j] % 2 == 0:
                    par_cor1 += 1
                else:
                    impar_cor1 += 1

    if par_cor1 + impar_cor0 < par_cor0 + impar_cor1:
        custo = par_cor1 + impar_cor0
        cor0_deve_ser_par = True
    else:
        custo = par_cor0 + impar_cor1

    for i in range(n):
        for j in range(m):
            cor = (i + j) % 2

            if cor == 0:
                esperado_par = cor0_deve_ser_par
            else:
                esperado_par = not cor0_deve_ser_par

            atual_par = (b[i][j] % 2 == 0)

            if atual_par != esperado_par:
                b[i][j] = b[i][j] + 1

    print(custo)
    for i in range(n):
        print(" ".join(map(str, b[i])))


if __name__ == '__main__':
    main()
