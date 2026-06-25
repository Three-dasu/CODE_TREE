N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sA = set()
for n in A:
    sA.add(n)
sB = set()
for n in B:
    sB.add(n)

# A-B 구하기
A_B = set()
for n in A:
    if n not in sB:
        A_B.add(n)

# 대칭 차집합 구하기
for n in B:
    if n not in sA:
        A_B.add(n)

print(len(A_B))