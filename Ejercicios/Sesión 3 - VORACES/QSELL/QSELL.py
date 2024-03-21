def personas_seducidas(concursante, seduciones):

    # Cualidad preferida y tiempo máximo del concursante
    cualidad_valorada = concursante[0]
    tiempo_restante = concursante[1]

    # Para saber el índice del valor que se debe tener en cuenta
    def get_indice_cualidad(c):
        if c == "beauty":
            return 1
        elif c == "intelligence":
            return 2
        elif c == "kindness":
            return 3

    # Beneficio total a mostrar
    beneficio_total = 0

    # Índice de la cualidad preferida en la lista de seductores
    cualidad_tentacion = get_indice_cualidad(cualidad_valorada)
    # Se ordena la lista de seduciones en función del valor preferido en proporción al tiempo
    # Es decir, los más rápidos van los primeros
    seduciones = sorted(seduciones, key=lambda x: float(x[4]) / float(x[cualidad_tentacion]))
    idx_seductor = 0

    # Lista donde se guardan los seductores que han conseguido seducir al participante
    seductores_exitosos = []

    # Si queda tiempo y también quedan seductores por participar
    while tiempo_restante > 0 and not idx_seductor >= len(seduciones):
        seductor_actual = seduciones[idx_seductor]
        # Si el tiempo del seductor es mayor al tiempo que le queda el concursante
        if int(seductor_actual[4]) > tiempo_restante:
            # Beneficio proporcional al tiempo que ha podido dedicar
            beneficio_total += (tiempo_restante * int(seductor_actual[cualidad_tentacion])) / int(seductor_actual[4])
            # Igualmente, se añade esta persona ya que no puede quedarse "a medias"
            seductores_exitosos.append(seductor_actual[0])
            # Se acaba el tiempo
            tiempo_restante = 0
        # En caso de que el tiempo del seductor sea suficiente
        else:
            # Se suman los puntos del seductor
            beneficio_total += int(seductor_actual[cualidad_tentacion])
            # Se resta el tiempo que le ha tomado
            tiempo_restante -= int(seductor_actual[4])
            # Se guarda como exitoso
            seductores_exitosos.append(seductor_actual[0])
            # Se actualiza el índice para pasar al siguiente
            idx_seductor += 1

    # Se devuelve la lista de las personas que lo han conseguido, y el beneficio total (formateado a dos decimales)
    return seductores_exitosos, format(beneficio_total, '.2f')


n = int(input().strip())
concursantes = []
tentaciones = []

for i in range(n):
    cualidad = input().strip()
    tiempoMax = int(input().strip())
    posiblesParejas = int(input().strip())
    pParejas = []

    for t in range(posiblesParejas):
        candidato = list(map(str, input().strip().split()))
        pParejas.append(candidato)

    tentaciones.append(pParejas)
    concursantes.append([cualidad, tiempoMax])

for i in range(n):
    [personasSeducidas, beneficio] = personas_seducidas(concursantes[i], tentaciones[i])
    for n in personasSeducidas:
        print(n, end=' ')
    print()
    print(beneficio)
