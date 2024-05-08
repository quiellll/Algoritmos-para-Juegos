import bisect

n = int(input().strip())
ln = list(map(int, input().strip().split()))

lvl_sum = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    lvl_sum[i] = ln[i - 1] + lvl_sum[i - 1]

m = int(input().strip())
for i in range(m):

    idx = bisect.bisect_right(ln, int(input().strip()))
    print(str(idx) + " " + str(lvl_sum[idx]))
