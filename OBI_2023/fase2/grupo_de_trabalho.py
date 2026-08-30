def main():
    e, m, d = map(int, input().split())
    li_m = []
    for _ in range(m):
        li_m.append(tuple(map(int, input().split())))
    li_d = []
    for _ in range(d):
        li_d.append(tuple(map(int, input().split())))

    g_e = [0] * (e + 1)

    for n_g in range(e // 3):
        i, j, k = map(int, input().split())
        g_e[i] = n_g
        g_e[j] = n_g
        g_e[k] = n_g

    vi = 0

    for x, y in li_m:
        if g_e[x] != g_e[y]:
            vi += 1

    for u, v in li_d:
        if g_e[u] == g_e[v]:
            vi += 1

    print(vi)


if __name__ == "__main__":
    main()
