def main():
    n = int(input())
    li = []
    d = 0

    for i in range(n):
        li.append(list(map(int, input().split())))

    for i in range(n):
        if li[i][0] > li[i][1]:
            d += li[i][1]

    print(d)


if __name__ == "__main__":
    main()
