def main():
    n = int(input())
    li = []
    for i in range(n):
        li.append(list(map(int, input().split())))

    s_r = sum(li[0])
    s_d1 = 0
    s_d2 = 0
    for i in range(n):
        s_d1 += li[i][i]
        s_d2 += li[i][n - 1 - i]

    if s_d1 != s_r or s_d2 != s_r:
        print(-1)
        return

    for i in range(n):
        if sum(li[i]) != s_r:
            print(-1)
            return

    s_c = [sum(coluna) for coluna in zip(*li)]

    for i in range(n):
        if s_c[i] != s_r:
            print(-1)
            return

    print(s_r)


if __name__ == '__main__':
    main()
