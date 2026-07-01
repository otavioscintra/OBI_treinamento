def main():
    n = int(input())
    li = []

    for i in range(n):
        num = int(input())
        if num == 0:
            if li:
                li.pop()
        else:
            li.append(num)

    print(sum(li))


if __name__ == "__main__":
    main()
