def factibilidad(lista):
    m = lista[0][2]
    candidato = lista[0]
    for i in range(len(lista)):
        if lista[i][2] < m:
            candidato = lista[i]

    return candidato

def hola(l, k):
    #solucion
    j = []
    v = []
    #bucle -> mientras el grupo de jovenes no esta lleno
    #PEOR MIGUEL COMO SE EL TAMAÑO DEL GRUPO? QUE TAMAÑO TIENEQUE TENER?
    idx = 0
    while len(j) + len(v) != len(l):

        #seleccion candidato
        #cojo el candidato q este iterando yasta
        cnd = l[idx]
        v.append(cnd)
        #factibilidad
        #me creo una funcion que me devbuelva el candidato con menor edad
        menor = factibilidad(v)
        #hago algo para quitarlo de los candidatos
        v.remove(menor)
        ##agregar a solucion: lo agrego a los jovenes
        j.append(menor)
        idx += 1
    #fin bucle

    #itero desde el ult candidato +1 a n y los meto en viejos
    return j, v


n, k = map(int, input().strip().split())

l = []

for _ in range(n):
    p, a = input().strip().split()

    l.append((p, int(a)))


