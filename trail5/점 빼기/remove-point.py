N, M = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(N)]
queries = [int(input()) for _ in range(M)]

from sortedcontainers import SortedSet
ss = SortedSet(points)

for k in queries:
    idx = ss.bisect_left((k, 1))

    if idx == len(ss):
        print("-1 -1")
    else:
        print(ss[idx][0], ss[idx][1])
        ss.remove((ss[idx][0], ss[idx][1]))

