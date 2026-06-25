N, M = map(int, input().split())
queries = list(map(int, input().split()))

from sortedcontainers import SortedSet
ss = SortedSet([x for x in range(1, M+1)])

for n in queries:
    ss.remove(n)

    print(ss[-1])
