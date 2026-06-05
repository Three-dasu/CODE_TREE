N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


dp = [[-1]*N for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(1, N):
    dp[i][0] = max(arr[i][0], dp[i-1][0])

for j in range(1, N):
    dp[0][j] = max(arr[0][j], dp[0][j-1])


for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(arr[i][j], min(dp[i-1][j], dp[i][j-1]))


print(dp[N-1][N-1])