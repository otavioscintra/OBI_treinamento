def main():
    num = list(map(int, input().split()))
    estoque = []
    for i in range(num[0]):
        estoque.append(list(map(int, input().split())))

    p = int(input())
    ped = []
    for i in range(p):
        ped.append(list(map(int, input().split())))

    vendidos = 0

    for pedido in ped:
        if estoque[pedido[0] - 1][pedido[1] - 1] > 0:
            estoque[pedido[0] - 1][pedido[1] - 1] -= 1
            vendidos += 1

    print(vendidos)


if __name__ == "__main__":
    main()
