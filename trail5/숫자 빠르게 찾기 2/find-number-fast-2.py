N, M = map(int, input().split())
from sortedcontainers import SortedSet
ss = SortedSet(map(int, input().split()))

# ss = SortedSet(lst)

for _ in range(M):
    n = int(input())

    idx = ss.bisect_left(n)
    # print(n, idx)
    if idx == len(ss):
        print(-1)
    else:
        print(ss[idx])

    