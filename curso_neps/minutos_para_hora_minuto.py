def main():
    m = int(input())

    h = m // 60

    m -= (h * 60)

    print(h)
    print(m)


if __name__ == "__main__":
    main()
