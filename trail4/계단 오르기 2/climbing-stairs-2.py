N = int(input())
coin = [0] + list(map(int, input().split()))

# dp[i][j]: i번째 계단까지 j번의 1계단 점프로 갔을 때의 최대 동전 개수
dp = [[-1]*(4) for _ in range(N+1)]
dp[0][0] = 0
dp[1][1] = coin[1]

for i in range(2, N+1):
    for j in range(4):
        
        # j가 0인 경우 -> 무조건 2계단 점프
        if j == 0 and dp[i-2][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])

        # 기존 vs 1계단 점프 vs 2계단 점프
        if 1 <= j <= 3:
            if dp[i-2][j] != -1:
                dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])

            if dp[i-1][j-1] != -1:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin[i])

            # if dp[i-1][j-1] != -1 and dp[i-2][j] != -1:
            #     dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin[i], dp[i-2][j] + coin[i])

print(max(dp[N]))
