N, M = map(int, input().split())

A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

"""
A의 문자열 집합과 B 문자열 집합의 교집합이 공집합

길이 3개 백트래킹
경우마다 A set 만들고 B 돌면서 A에 있나 확인
"""
def check(i, j, k, sa):
    for n in range(N):
        if (B[n][i], B[n][j], B[n][k]) in sa:
            return False
    return True
cnt = 0

for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            sa = set()
            for n in range(N):
                sa.add((A[n][i], A[n][j], A[n][k]))
            
            for n in range(N):
                if check(i, j, k, sa):
                    # print(i, j, k)
                    cnt += 1
                    break

print(cnt)

                    