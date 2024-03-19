def IndiceCualidad(cualidad):
    if cualidad == "beauty":
        return 1
    elif cualidad == "intelligence":
        return 2
    elif cualidad == "kindness":
        return


def OrdenarPretendientes(pretendientes, indiceCualidad):
    pretendientes = sorted(pretendientes, key=lambda x:
        float(x[4])/float(x[indiceCualidad]))
    return pretendientes


def PersonasSeducidas(cualidadValorada, tiempoRestante, posiblesParejas):
    beneficio = 0
    indiceCualidad = IndiceCualidad(cualidadValorada)
    posiblesParejas = OrdenarPretendientes(posiblesParejas, indiceCualidad)
    personasSeducidas = []
    i = 0
    while tiempoRestante > 0 and not i >= len(posiblesParejas):
        if int(posiblesParejas[i][4]) > tiempoRestante: #si el tiempo para seducir a la persona q toca supera el tiempo restante
            beneficio += (tiempoRestante*int(posiblesParejas[i][indiceCualidad]))/int(posiblesParejas[i][4]) #beneficio proporcional al tiempo empleado
            format(beneficio, '.2f')
            personasSeducidas.append(posiblesParejas[i][0])
            tiempoRestante = 0
        else:
            beneficio += int(posiblesParejas[i][indiceCualidad])
            tiempoRestante-= int(posiblesParejas[i][4])
            personasSeducidas.append(posiblesParejas[i][0])
            i += 1
    return personasSeducidas, format(beneficio, '.2f')


nConcursantes = int(input())
concursantes = []
posiblesParejas = []

for i in range(nConcursantes):
    cualidadMasValorada = input()
    tiempoRestante = int(input())
    nPosiblesParejas = int(input())
    pParejas = []
    for t in range(nPosiblesParejas):
        pretendiente = list(map(str,input().split()))
        pParejas.append(pretendiente)
    posiblesParejas.append(pParejas)
    concursantes.append([cualidadMasValorada, tiempoRestante])

for i in range(nConcursantes):
    [personasSeducidas, beneficio] = PersonasSeducidas(concursantes[i][0], concursantes[i][1], posiblesParejas[i])
    for nombre in personasSeducidas:
        print(nombre, end = " ")
    print()
    print(beneficio)