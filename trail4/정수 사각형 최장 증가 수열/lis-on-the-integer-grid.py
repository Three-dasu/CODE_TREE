def in_range(i, j):
    return 0<=i<N and 0<=j<N

def myp(arr):
    for row in arr:
        for val in row:
            print(val, end=' ')
        print()
    print()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1]*N for _ in range(N)]
ans = 0

def func(i, j):
    
    if dp[i][j] > -1:
        return dp[i][j]
    
    dp[i][j] = 1

    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni, nj = i+di, j+dj

        if in_range(ni, nj) and arr[ni][nj] > arr[i][j]:
            dp[i][j] = max(dp[i][j], func(ni, nj)+1)
    
    # myp(dp)
    return dp[i][j]


for i in range(N):
    for j in range(N):
        ans = max(ans, func(i, j))

print(ans)