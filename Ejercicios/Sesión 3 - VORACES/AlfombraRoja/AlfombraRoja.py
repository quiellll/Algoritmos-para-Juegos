def ordenar_famosos(famosos):
    mas_amable = famosos[0]

    for f in famosos:
        # String < String para ordenar alfabéticamente
        if f[1] < mas_amable[1]:
            mas_amable = f

    idx = 0
    tiempo_mas_amable = 0

    while idx < famosos.index(mas_amable):
        tiempo_mas_amable += famosos[idx][4]
        idx += 1

    for f in famosos:
        print(f[1])

    print(tiempo_mas_amable)


n_famosos = int(input().strip())
famosos = []

for _ in range(n_famosos):
    nombre, amabilidad, fama, tiempo = map(str, input().strip().split())
    famoso = [(int(amabilidad)/int(fama)), nombre, int(amabilidad), int(fama), int(tiempo)]
    famosos.append(famoso)

famosos.sort()
ordenar_famosos(famosos)
