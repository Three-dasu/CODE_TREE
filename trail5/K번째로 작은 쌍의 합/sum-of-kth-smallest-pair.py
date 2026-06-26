N, M, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

"""
두 수열에서 원소 하나씩 뽑아 나오는 쌍들 생성
그것들을 오름차순 나열
K번째 쌍의 합
1 <= N, M <= 10만
k도 최대가 10만
조합 자체는 백트래킹 하면 O(NxM) 벌써 터짐

얘도 보니까 뭔가 새로운 걸 해야 해
dp에선 요런 느낌은 첫 숫자에서 나올 수 있는 경우의 수를
K에서 빼면서 경우의 수를 줄였는데
"""

import heapq as hf
hq = []

a.sort()
b.sort()

i, j = 0, 0
hq = [(a[i]+b[j], i, j)]
v = set()
v.add((i, j))
cnt = 0

while hq:
    # print(hq)
    # print(v)
    ab, i, j = hf.heappop(hq)
    cnt += 1
    
    if cnt == K:
        print(ab)
        break
    
    for di, dj in ((0, 1), (1, 0)):
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and (ni, nj) not in v:
            hf.heappush(hq, (a[ni]+b[nj], ni, nj))
            v.add((ni, nj))

    
