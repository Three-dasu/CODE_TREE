N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

"""
수열에서 두 수를 골라, 차이가 M 이상인 경우 중 차이의 최솟값 구하기

수열에서 하나를 골라 그거보다 M "이상" 큰 수 중에 처음인 수를 찾기
이걸 모든 수에 대해 반복
"""
from sortedcontainers import SortedSet
ss = SortedSet(lst)

INF = float('inf')
ans = INF
for n in lst:
    num = n + M

    idx = ss.bisect_left(num)
    if idx == len(ss):
        continue
    snum = ss[idx]

    ans = min(ans, snum-n)

print(-1 if ans==INF else ans)