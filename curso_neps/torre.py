def main():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    p = 0
    m_p = 0

    s_l = [sum(linha) for linha in matrix]
    s_c = [sum(coluna) for coluna in zip(*matrix)]

    for i in range(n):
        for j in range(n):
            p = s_l[i] + s_c[j] - (2 * matrix[i][j])

            if p > m_p:
                m_p = p
            p = 0

    print(m_p)


if __name__ == "__main__":
    main()
