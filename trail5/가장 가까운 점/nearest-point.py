N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

import heapq as hp
hq = []

for x, y in points:
    hp.heappush(hq, (x+y, x, y))

for _ in range(M):
    (tot, x, y) = hp.heappop(hq)
    hp.heappush(hq, (tot+4, x+2, y+2))

print(hq[0][1], hq[0][2])