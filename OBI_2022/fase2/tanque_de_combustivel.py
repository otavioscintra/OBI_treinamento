def main():
    c = int(input())
    d = int(input())
    t = int(input())

    g = (d / c) - t if (d / c) - t > 0 else 0.0

    print(f'{g:.1f}')


if __name__ == "__main__":
    main()
