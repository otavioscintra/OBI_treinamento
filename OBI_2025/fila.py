def main():
    alunos = int(input())
    alturas = list(input())
    sem_ver = 0
    indice = alunos - 1

    for i in range(alunos - 1):
        while indice > 0:
            if alturas[indice] >= alturas[indice - 1] \
                  and alturas[indice - 1] > alturas[indice + 1]:
                sem_ver += 1
            indice -= 1
        indice = alunos - 1

    print(sem_ver)


if __name__ == '__main__':
    main()

# ainda n tá pronto
