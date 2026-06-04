N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

def init():
    dp[0][0] = arr[0][0]
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0], arr[i][0])

    for j in range(1, N):
        dp[0][j] = max(dp[0][j-1], arr[0][j])

def solve(lb):
    for i in range(N):
        for j in range(N):
            if arr[i][j] < lb:
                arr[i][j] = 2**31
    
    init()

    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), arr[i][j])
    
    return dp[N-1][N-1]

ans = 2**31
for lb in range(1, 101):
    ub = solve(lb)

    if ub == 2**31:
        continue
    
    ans = min(ans, ub-lb)

print(ans)