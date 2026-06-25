N, K = map(int, input().split())
lst = list(map(int, input().split()))

from sortedcontainers import SortedSet
ss = SortedSet(lst)

for i in range(-1, -K-1, -1):
    print(ss[i], end=' ')

