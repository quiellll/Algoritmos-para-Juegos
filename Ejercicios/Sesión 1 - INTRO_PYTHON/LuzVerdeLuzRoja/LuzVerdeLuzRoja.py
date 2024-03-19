i = input().strip().split()

if i[1] == "r" and i[2] == "1":
    print("JUGADOR " + str(i[0]) + " ELIMINADO")
else:
    print("JUGADOR " + str(i[0]) + " CONTINUAR")
