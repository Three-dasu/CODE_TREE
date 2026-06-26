N = int(input())
x = [int(input()) for _ in range(N)]

import heapq as hf

hq = []
for n in x:
    if n != 0:
        hf.heappush(hq, (abs(n), n))
    else:
        if not hq:
            print(0)
            continue
        absn, n = hf.heappop(hq)
        print(n)

