N = int(input())
lst = list(map(int, input().split()))

from sortedcontainers import SortedDict

adf = SortedDict()

for i, n in enumerate(lst):
    if n in adf:
        continue
    else:
        adf[n] = i

for k, v in adf.items():
    print(k, v+1)