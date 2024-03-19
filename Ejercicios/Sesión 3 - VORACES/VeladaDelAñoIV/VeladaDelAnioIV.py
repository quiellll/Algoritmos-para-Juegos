



n_actividades = int(input().strip())
actividades= []

for _ in range(n_actividades):
    n_actividad, t_ini, t_fin = map(int, input().strip().split())
    actividades.append([n_actividad, t_ini, t_fin])

print(calc_actividades)
