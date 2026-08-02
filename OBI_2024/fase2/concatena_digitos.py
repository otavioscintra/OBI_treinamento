def main():
    n, q = map(int, input().split())
    li_n = list(map(int, input().split()))

    for _ in range(q):
        p = 0
        l, r = map(int, input().split())
        li_q = li_n[l-1:r]
        li_p = []

        if l == r:
            print(0)
            continue

        for i in range(len(li_q)):
            for j in range(len(li_q)):
                if i != j:
                    li_p.append(f'{li_q[i]}{li_q[j]}')

        for i in range(len(li_p)):
            p += int(li_p[i])

        print(p)


if __name__ == "__main__":
    main()
