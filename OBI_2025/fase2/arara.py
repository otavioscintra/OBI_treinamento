def main():
    n, m = map(int, input().split())

    g_v = m - n

    if g_v >= 4 * (n - 1):
        print('S')
    else:
        print('N')


if __name__ == "__main__":
    main()
