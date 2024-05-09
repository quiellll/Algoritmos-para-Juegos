def personas_seducidas(concursante, seduciones):

    cualidad_valorada = concursante[0]
    tiempo_restante = concursante[1]

    def get_indice_cualidad(c):
        if c == "beauty":
            return 1
        elif c == "intelligence":
            return 2
        elif c == "kindness":
            return 3

    beneficio_total = 0

    cualidad_tentacion = get_indice_cualidad(cualidad_valorada)

    seduciones = sorted(seduciones, key=lambda x: float(x[4]) / float(x[cualidad_tentacion]))
    idx_seductor = 0

    seductores_exitosos = []

    while tiempo_restante > 0 and not idx_seductor >= len(seduciones):
        seductor_actual = seduciones[idx_seductor]

        if int(seductor_actual[4]) > tiempo_restante:
            beneficio_total += (tiempo_restante * int(seductor_actual[cualidad_tentacion]))
            seductores_exitosos.append(seductor_actual[0])
            tiempo_restante = 0
        else:
            beneficio_total += int(seductor_actual[cualidad_tentacion])
            tiempo_restante -= int(seductor_actual[4])
            seductores_exitosos.append(seductor_actual[0])
            idx_seductor += 1

    return seductores_exitosos, format(beneficio_total, '.2f')

n = int(input().strip())
concursantes = []
tentaciones = []

for _ in range(n):
    cualidad = input().strip()
    tiempoMax = int(input().strip())
    posiblesParejas = int(input().strip())
    pParejas = []

    for _ in range(posiblesParejas):
        candidato = list(map(str, input().strip().split()))
        pParejas.append(candidato)

    tentaciones.append(pParejas)
    concursantes.append([cualidad, tiempoMax])

for i in range(n):
    [personasSeducidas, beneficio] = personas_seducidas(concursantes[i], tentaciones[i])

    for n in personasSeducidas():
        print(n, end=' ')
    print()
    print(beneficio)

