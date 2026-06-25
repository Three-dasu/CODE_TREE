N, M = map(int, input().split())
lst = list(map(int, input().split()))

import heapq as hp

hq = []
for n in lst:
    hp.heappush(hq, -n)

for _ in range(M):
    n = hp.heappop(hq)
    hp.heappush(hq, n+1)

print(-hq[0])
