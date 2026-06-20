A = input()
B = input()

N = len(A)
M = len(B)

A = ' ' + A
B = ' ' + B

# dp[i][j]: i개의 A를 활용해서 j개의 B를 만들 수 있는 최소 연산 횟수
INF = float('inf')
dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    dp[i][0] = i

for j in range(1, M+1):
    dp[0][j] = j

for i in range(1, N+1):
    for j in range(1, M+1):
        
        if A[i] == B[j]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1])

        else:
            # 삽입
            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

            # 삭제
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)

            # # 교체
            # dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
print(dp[N][M])

