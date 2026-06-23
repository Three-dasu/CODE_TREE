n = int(input())
words = [input() for _ in range(n)]

from sortedcontainers import SortedDict

adf = SortedDict()

for c in words:
    if c in adf:
        adf[c] += 1
    else:
        adf[c] = 1

for c, v in adf.items():
    print(c, '{:.4f}'.format(100*adf[c]/n, 5))
