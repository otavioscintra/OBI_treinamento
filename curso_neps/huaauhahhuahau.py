def main():
    li = list(input())
    v = ['a', 'e', 'i', 'o', 'u']

    li_v = [p for p in li if p in v]

    inv_li_v = li_v[::-1]

    if li_v == inv_li_v:
        print('S')
    else:
        print('N')


if __name__ == '__main__':
    main()
