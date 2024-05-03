import bisect

n = int(input().strip())
niveles = list(map(int, input().strip().split()))

suma = [0] * (n + 1)

for i in range(1, n + 1):
    suma[i] = suma[i - 1] + niveles[i - 1]

m = int(input().strip())
q = []
for _ in range(m):
    q.append(int(input().strip()))

resultado = []
for n_caballero in q:
    index = bisect.bisect_right(niveles, n_caballero)
    enemigos = index
    ptos_totales = suma[index]
    resultado.append(f"{enemigos} {ptos_totales}")

print("\n".join(resultado))
