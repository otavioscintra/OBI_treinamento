def main():
    d = int(input())

    p = d / 400

    if p - int(p) <= 0.5:
        p = int(p)
    else:
        p = int(p + 1)

    print(abs(d - (400 * p)))


if __name__ == '__main__':
    main()
