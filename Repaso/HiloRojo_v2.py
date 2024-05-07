def obtener_indice(lista, inferior, superior, objetivo):

    if inferior > superior:
        return -1
    else:
        puntero = (inferior + superior) // 2

        if lista[puntero] == objetivo:
            return puntero
        else:
            if lista[puntero] > objetivo:
                return obtener_indice(lista, inferior, puntero - 1, objetivo)
            else:
                return obtener_indice(lista, puntero + 1, superior, objetivo)


n = int(input().strip())
l1 = input().strip().split()
grupo1 = [] * n
for i in range(n):
    grupo1.append(int(l1[i]))

m = int(input().strip())
l2 = input().strip().split()
grupo2 = [] * m
for i in range(m):
    grupo2.append(int(l2[i]))

p = int(input().strip())
for i in range(p):
    obj1, obj2 = map(int, input().strip().split())
    idx1 = obtener_indice(grupo1, 0, n - 1, obj1)
    idx2= obtener_indice(grupo2, 0, m - 1, obj2)
    if idx1 >= 0 and idx2 >= 0:
        print(str(idx1) + " " + str(idx2))
    else:
        print("SIN DESTINO")
