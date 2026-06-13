N = int(input())
lst = [0] + list(map(int, input().split()))

# dp[i][j]: i번째 계단까지 j번의 1계단 점프로 갔을 때의 최대 동전 개수
dp = [[-1]*(4) for _ in range(N+1)]
dp[0][0] = 0
dp[1][1] = lst[1]

for i in range(N):
    for j in range(4):
        if dp[i][j] != -1:
            # j가 3인 경우 -> 1계단 점프 불가 -> 기존 vs 2계단 점프
            if j == 3 and i <= N-2:
                dp[i+2][j] = max(dp[i+2][j], dp[i][j] + lst[i+2])

            # 기존 vs 1계단 점프
            if j <= 2:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + lst[i+1])

            if i <= N-2:
                dp[i+2][j] = max(dp[i+2][j], dp[i][j] + lst[i+2])

print(max(dp[N]))