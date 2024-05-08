def bin_search(arr, trg, lo, hi):
    if lo > hi:
        return -1
    else:
        mid = (lo + hi) // 2
        if arr[mid] == trg:
            return mid
        else:
            if arr[mid] > trg:
                return bin_search(arr, trg, lo, mid - 1)
            else:
                return bin_search(arr, trg, mid + 1, hi)


n = int(input())
ln1 = list(map(int, input().split()))
gr1 = [0 for _ in range(n)]
for i in range(n):
    gr1[i] = ln1[i]

m = int(input())
ln2 = list(map(int, input().split()))
gr2 = [0 for _ in range(m)]
for i in range(m):
    gr2[i] = ln2[i]

p = int(input())
for i in range(p):
    a, b = map(int, input().split())
    idx1 = bin_search(gr1, a, 0, n - 1)
    idx2 = bin_search(gr2, b, 0, m - 1)

    if idx1 >= 0 and idx2 >= 0:
        print(str(idx1) + " " + str(idx2))
    else:
        print("SIN DESTINO")
