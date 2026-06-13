N = int(input())
red = []
blue = []

for _ in range(2 * N):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# dp[i][j]: 빨간색 i개, 파란색 j개 선택했을 때 최댓값
dp = [[-1]*(N+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(N+1):
        if (i, j) == (N, N):
            continue
        
        # 몇번째 카드인지
        n = i + j
        r, b = red[n], blue[n]

        # 빨강 선택
        if i < N:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+r)

        # 파랑 선택
        if j < N:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j]+b)

print(dp[N][N])