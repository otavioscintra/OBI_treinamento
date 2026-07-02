def main():
    s = input().lower()
    li = list(s)
    n = []

    for i in range(len(li)):
        if li[i] == "-":
            n.append("-")

        match li[i]:
            case 'a' | 'b' | 'c':
                n.append('2')
            case 'd' | 'e' | 'f':
                n.append('3')
            case 'g' | 'h' | 'i':
                n.append('4')
            case 'j' | 'k' | 'l':
                n.append('5')
            case 'm' | 'n' | 'o':
                n.append('6')
            case 'p' | 'q' | 'r' | 's':
                n.append('7')
            case 't' | 'u' | 'v':
                n.append('8')
            case 'w' | 'x' | 'y' | 'z':
                n.append('9')

    num = "".join(n)

    print(num)


if __name__ == "__main__":
    main()
