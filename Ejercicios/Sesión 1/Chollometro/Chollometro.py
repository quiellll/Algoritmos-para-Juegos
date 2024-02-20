usos = input().strip().split()
destacado = -1
destacadoidx = -1
indice = 0

for cupon in usos:
    indice = indice + 1
    if int(cupon) > int(destacado):
        destacado = cupon
        destacadoidx = indice
    barras = ""
    for n in range(int(cupon)):
        barras = barras + "="
    print(str(indice) + " " + barras)

print("El mas usado es el cupon " + str(destacadoidx) + " con " + str(destacado) + " usos")
