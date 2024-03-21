def seleccionar_actividades(actividades):
    # Ordenar por el tiempo de finalización
    actividades.sort(key=lambda x: x[2])

    # Contador de las actividades que se pueden hacer
    actividades_realizadas = 0

    # El tiempo en el que acaba la última actividad que se ha seleccionado
    t_fin_ultima_act_seleccionada = -1

    for actividad in actividades:
        # Si la actividad actual comienza después (o a la vez) que la anterior,
        # la contamos como válida
        if actividad[1] >= t_fin_ultima_act_seleccionada:
            actividades_realizadas += 1
            t_fin_ultima_act_seleccionada = actividad[2]    # Actualizar la variable

    return actividades_realizadas


n_actividades = int(input().strip())
total_actividades = []

for _ in range(n_actividades):
    n_actividad, t_ini, t_fin = map(str, input().strip().split())
    # t_total = int(t_fin) - int(t_ini)
    total_actividades.append([n_actividad, int(t_ini), int(t_fin)])

print(seleccionar_actividades(total_actividades))
