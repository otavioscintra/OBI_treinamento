def main():
    k, n = map(int, input().split())
    li_k = list(map(str, input().strip()))
    li_n = list(map(str, input().strip()))

    for i in li_n:
        if i not in li_k:
            print('N')
            return

    print('S')


if __name__ == "__main__":
    main()
