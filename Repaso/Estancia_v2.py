def backtrack(objetos, mochila, seleccionados, costeAct, benefAct, mejorBenef, mejorCost, mejorMochila, x):
    if esSolucion(mochila, costeAct, objetos):
        if benefAct > mejorBenef:
            mejorBenef = benefAct
            mejorCost = costeAct
            mejorMochila = mochila.copy()
        return mejorMochila, mejorBenef, mejorCost
    else:
        for k in range(x, len(objetos)):
            o = objetos[k]
            if esFactible(o, seleccionados, costeAct):
                mochila.append(o)
                seleccionados.add(o)
                costeAct += o[1]
                benefAct += o[2]
                mejorMochila, mejorBenef, mejorCost = backtrack(objetos, mochila, seleccionados, costeAct, benefAct, mejorBenef, mejorCost, mejorMochila, k+1)
                mochila.pop()
                seleccionados.remove(o)
                costeAct -= o[1]
                benefAct -= o[2]
    return mejorMochila, mejorBenef, mejorCost


def esSolucion(mochila, actCost, objetos):
    min_peso = 0x3f3f3f
    for o in objetos:
        if o not in mochila and min_peso > o[1]:
            min_peso = o[1]
    return actCost + min_peso > p


def esFactible(o, seleccionado, actCost):
    return actCost + o[1] <= p and (o not in seleccionado)


n, p, b = map(int, input().strip().split())
objetos = []

for _ in range(n):
    name, cost, profit = input().strip().split()
    objetos.append((name, int(cost), int(profit)))

mochila = []
seleccionados = set()

mejor_mochila, mejorBeneficio, mejorCoste = backtrack(objetos, mochila, seleccionados, 0, 0, 0, 0, [], 0)
mejor_mochila.sort()

for o in mejor_mochila:
    print(o[0], end=" ")

print()
print(mejorCoste, mejorBeneficio)

if mejorBeneficio > b:
    print("SE VA")
else:
    print("VUELVE")
