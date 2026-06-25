N, M = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(N)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(M)]

from sortedcontainers import SortedSet
ss = SortedSet()

for x, y in points:
    ss.add((x, y))

for x, y in queries:
    idx = ss.bisect_left((x, y))
    if idx == N:
        print('-1 -1')
    else:
        x, y = ss[idx]
        print(x, y)