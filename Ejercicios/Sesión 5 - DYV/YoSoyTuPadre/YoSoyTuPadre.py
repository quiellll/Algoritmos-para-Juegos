from collections import deque

def construir_arbol(miembros):
    arbol = {}
    for miembro in miembros:
        padre = miembro[0]
        hijos = miembro[1:]
        arbol[padre] = hijos
    return arbol

def calcular_niveles(arbol, raiz):
    niveles = {}
    cola = deque([(raiz, 1)])
    while cola:
        miembro, nivel = cola.popleft()
        niveles[miembro] = nivel
        hijos = arbol.get(miembro, [])
        for hijo in hijos:
            cola.append((hijo, nivel + 1))
    return niveles

def calcular_generaciones(miembros, consultas):
    arbol = construir_arbol(miembros)
    padres = set()
    hijos = set()

    for miembro in miembros:
        padres.add(miembro[0])
        hijos.update(miembro[1:])

    raiz = list(padres - hijos)[0]
    niveles = calcular_niveles(arbol, raiz)
    resultados = [niveles[consulta] for consulta in consultas]
    return resultados


# Entrada
n = int(input().strip())
miembros = [list(map(int, input().strip().split())) for _ in range(n)]

m = int(input().strip())
consultas = [int(input().strip()) for _ in range(m)]

# Cálculo y salida
resultados = calcular_generaciones(miembros, consultas)
for resultado in resultados:
    print(resultado)
