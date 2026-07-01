from statistics import multimode


def main():
    n = int(input())
    li = []

    for i in range(n):
        li.append(int(input()))

    f = multimode(li)

    f.sort()

    s = " ".join(map(str, f))

    print(s)


if __name__ == "__main__":
    main()
