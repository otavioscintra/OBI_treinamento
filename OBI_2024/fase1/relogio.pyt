def main():
    h = int(input())
    m = int(input())
    s = int(input())
    t = int(input())

    s += t

    if s >= 60:
        m += s // 60
        s -= (s // 60) * 60

    if m >= 60:
        h += m // 60
        m -= (m // 60) * 60

    if h >= 24:
        h -= (h // 24) * 24

    print(h)
    print(m)
    print(s)


if __name__ == '__main__':
    main()
