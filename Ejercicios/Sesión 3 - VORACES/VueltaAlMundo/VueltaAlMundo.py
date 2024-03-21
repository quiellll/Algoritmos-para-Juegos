def seleccionar_paises(lista_intervalos_paises):
    # Ordenar por el mes de salida
    paises_ordenados = sorted(lista_intervalos_paises, key=lambda x: x[1])

    paises_seleccionados = 0
    ultimo_salida = -1

    for pais in paises_ordenados:
        if pais[0] >= ultimo_salida:
            paises_seleccionados += 1
            ultimo_salida = pais[1]

    return paises_seleccionados


v = int(input().strip())

for _ in range(v):
    p = int(input().strip())

    # Almacenar los intervalos de la organización
    meses_p = list(map(int, input().strip().split()))

    # Convertir los intervalos a tuplas
    paises = [(meses_p[i], meses_p[i + 1]) for i in range(0, len(meses_p), 2)]

    # Seleccionar los paises con el algoritmo voraz
    print(seleccionar_paises(paises))
