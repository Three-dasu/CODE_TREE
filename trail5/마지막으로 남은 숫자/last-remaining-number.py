N = int(input())
lst = list(map(int, input().split()))

import heapq
hq = []

for n in lst:
    heapq.heappush(hq, -n)

while len(hq) >= 2:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)

    if a == b:
        continue
    else:
        heapq.heappush(hq, a-b)

if hq:
    print(-hq[0])
else:
    print(-1)