N = int(input())
queries = list(map(int, input().split()))

from sortedcontainers import SortedSet
ss = SortedSet()
ss.add(0)
INF = float('inf')

ans = INF
for n in queries:
    idx = ss.bisect_right(n)

    # 더 큰 숫자 없으면
    if idx == len(ss):
        left, right = n-ss[-1], INF
    else:
        left, right = n-ss[idx-1], ss[idx]-n
    
    ans = min(ans, left, right)
    print(ans)
    ss.add(n)
