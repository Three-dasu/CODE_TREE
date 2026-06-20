A = " " + input()
B = " " + input()
N = len(A) - 1
M = len(B) - 1
"""
문자열 A를 문자열 B로 바꾸기 위한 최소 연산 횟수

dp[i][j]: A[:i+1]를 B[:j+1]로 바꾸기 위한 최소 연산 횟수
"""

INF = float('inf')
dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    dp[i][0] = i

for j in range(1, M+1):
    dp[0][j] = j



for i in range(N+1):
    for j in range(M+1):
        if dp[i][j] == INF:
            continue
        
        if i<N and j<M and A[i+1] == B[j+1]:
            dp[i+1][j+1] = dp[i][j]

        else:
            # 삽입
            if j < M:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)


            # 삭제
            if i < N:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)

            if i<N and j<M:
                # 바꾸기
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + 1)

print(dp[N][M])