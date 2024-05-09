def agrupar(part, k):
    g1 = []
    for _ in range(k):
        g1.append(part.pop(0))

    for p in g1:
        print(p[1], end=" ")
    print()
    for p in part:
        print(p[1], end=" ")


n, k, = map(int, input().strip().split())
participantes = []

for _ in range(n):
    n, e = map(int, input().strip().split())
    participantes.append((e, n))

    participantes.sort()
    agrupar(participantes, min(n - k, k))
