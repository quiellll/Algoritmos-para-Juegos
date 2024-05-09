def seleccionar_actividades(actividades):

    actividades_realizadas = 0

    t_fin_ultima = -1

    for t_f, act, t_i in actividades:
        if t_i >= t_fin_ultima:
            actividades_realizadas += 1
            t_fin_ultima = t_f

    return actividades_realizadas


n_act = int(input().strip())

total_act = []

for _ in range(n_act):
    n_act, t_ini, t_fin = map(str, input().strip().split())
    total_act.append([int(t_fin), n_act, int(t_ini)])

total_act.sort()
print(seleccionar_actividades(total_act))


