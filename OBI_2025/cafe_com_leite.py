def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    livre = c - d

    if livre >= a and livre <= b:
        print("S")
    else:
        print("N")


if __name__ == "__main__":
    main()
