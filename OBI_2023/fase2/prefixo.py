def main():
    n = int(input())
    p = list(input().strip())
    m = int(input())
    s = list(input().strip())

    menor = m if m <= n else n
    c = 0
    i = 0

    while i < menor and p[i] == s[i]  :
        c += 1
        i += 1

    print(c)


if __name__ == '__main__':
    main()
