def main():
    e_p = list(map(int, input().split()))
    p = e_p[0]
    m_p = e_p[1:]
    e_c = list(map(int, input().split()))
    c = e_c[0]
    m_c = e_c[1:]

    p_p = [[m, 'P'] for m in m_p]
    p_c = [[m, 'C'] for m in m_c]

    t_p = p_p + p_c
    t_p.sort()

    g_p = 0
    g_c = 0

    placar = ['0 0']

    for i in t_p:

        if i[1] == 'P':
            g_p += 1
        else:
            g_c += 1

        placar.append(f'{g_p} {g_c}')

    for i in placar:
        print(i)


if __name__ == "__main__":
    main()
