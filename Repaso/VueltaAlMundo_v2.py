def seleccionar_paises(lista):

    paises_ordenados = sorted(lista, key=lambda x: x[1])

    paises_seleccionados = 0
    ultimo = -1

    for pais in paises_ordenados:
        if pais[0] >= ultimo:
            paises_seleccionados += 1
            ultimo = pais[1]

    return paises_seleccionados


v = int(input().strip())

for _ in range(v):
    p = int(input().strip())

    meses_p = list(map(int, input().strip().split()))

    paises = [(meses_p[i], meses_p[i+1]) for i in range(0, len(meses_p), 2)]

    print(seleccionar_paises(paises))
