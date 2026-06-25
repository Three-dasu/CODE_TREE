n = int(input())
x = [int(input()) for _ in range(n)]

import heapq as hp
hq = []

for n in x:
    if n == 0:
        if not hq:
            print(0)
            continue
        print(hp.heappop(hq))
    else:
        hp.heappush(hq, n)