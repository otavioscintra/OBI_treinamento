def main():
    n, m, p = map(int, input().split())

    l_a = list(range(n))
    c_a = list(range(m))

    for _ in range(p):
        partes = input().split()
        op = partes[0]
        a = int(partes[1])
        b = int(partes[2])

        if op == 'L':
            l_a[a-1], l_a[b-1] = l_a[b-1], l_a[a-1]
        else:
            c_a[a-1], c_a[b-1] = c_a[b-1], c_a[a-1]

    resultado = []

    for i in range(n):
        valores = [l_a[i] * m + c_a[j] + 1 for j in range(m)]
        linha_str = ' '.join(map(str, valores))
        resultado.append(linha_str)

    print('\n'.join(resultado))


if __name__ == "__main__":
    main()
