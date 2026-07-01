N, M = map(int, input().split())
lst = list(map(int, input().split()))
query = list(map(int, input().split()))

from sortedcontainers import SortedSet
ss = SortedSet(lst)

for x in query:
    idx = ss.bisect_right(x)

    if idx == 0 or idx == N:
        print(-1)
        continue
    
    print(ss[idx-1])
    ss.remove(ss[idx-1])
    


