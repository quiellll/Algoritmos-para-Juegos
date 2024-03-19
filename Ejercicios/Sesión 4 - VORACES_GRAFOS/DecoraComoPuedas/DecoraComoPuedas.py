from queue import PriorityQueue

def dijkstra(g):
    n = len(g)
    q = PriorityQueue()



n, m, t = map(int, input().strip().split())
habitaciones = [[] for _ in range(n)]

for _ in range(m):
    h_1, h_2, d = map(int, input().strip().split())
    habitaciones[h_1].append([h_2, d])
    habitaciones[h_2].append([h_1, d])
