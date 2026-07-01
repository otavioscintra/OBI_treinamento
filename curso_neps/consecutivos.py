def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = 1
    m_c = 0

    for i in range(n - 1):
        if v[i] == v[i + 1]:
            c += 1
        else:
            c = 1
        if c > m_c:
            m_c = c

    print(m_c)


if __name__ == "__main__":
    main()
