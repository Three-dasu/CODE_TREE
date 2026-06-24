N, K = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(K)]
# edges = [(a-1, b-1) for (a, b) in edges]

"""
1~N 이라는 자리에 앉은 사람들이 자리를 바꿈
근데 또바꿈
금데 또 바꿈

곧이곧대로 하면 시간초과... 가 아닌가 3x10^5네
"""

# m2p = [x for x in range(N)]  # idx:사람 v:위치
p2m = [x for x in range(N+1)]  # idx:위치 v:사람
slst = [set() for _ in range(N+1)]
for i in range(1, N+1):
    slst[i].add(i)

for _ in range(3):
    for a, b in edges:
        # [1] a, b 위치에 있는 사람 불러오고
        m1, m2 = p2m[a], p2m[b]
        # [2] 자리 체인지
        p2m[a], p2m[b] = m2, m1

        # print(m1, m2, 'moved')
        # print('from', a, b, 'to', b, a)

        slst[m1].add(b)
        slst[m2].add(a)

for a in slst[1:]:
    print(len(a))




