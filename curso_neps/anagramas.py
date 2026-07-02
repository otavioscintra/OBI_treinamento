def main():
    n = int(input())
    a = input().replace(" ", "").replace(",", "").replace(".", "")
    b = input().replace(" ", "").replace(",", "").replace(".", "")

    l_a = sorted(a)
    l_b = sorted(b)

    if l_a == l_b:
        print('S')
    else:
        print('N')


if __name__ == '__main__':
    main()
