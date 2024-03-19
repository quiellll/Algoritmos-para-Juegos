C = int(input())    # Número de capturas

idx = 0
first = [-1, -1]
second = [-1, -1]
puntuacion = -1

for i in range(int(C)):
    info = input().strip().split()  # ID + espacio + puntuación

    if int(info[1]) > int(first[1]):
        second[0] = int(first[0])
        second[1] = int(first[1])
        first[0] = int(info[0])
        first[1] = int(info[1])
    elif int(int(info[1]) > second[1]):
        second[0] = int(info[0])
        second[1] = int(info[1])

    puntuacion = int(first[1]) + int(second[1])
    idx = idx + 1


print(str(first[0]) + " " + str(second[0]) + " " + str(puntuacion))
