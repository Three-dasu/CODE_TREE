N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# dp[i][j]: i층에서 j번째 방을 들어갔을 때 최대 보물 수
dp = [[-1]*(M) for _ in range(N)]
for j in range(M):
    dp[0][j] = arr[0][j]

for i in range(N-1):
    for j in range(M):
        if dp[i][j] == -1:
            continue
        
        for k in range(M):  # 다음 층 방
            if j == k:
                continue
            
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + arr[i+1][k])

print(max(dp[N-1]))