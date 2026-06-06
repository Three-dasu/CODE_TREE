N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
dp[0][0] = 1

for ci in range(N):
    for cj in range(M):
        

        for ni in range(ci+1, N):
            for nj in range(cj+1, M):

                if arr[ni][nj] > arr[ci][cj]:
                    dp[ni][nj] = max(dp[ni][nj], dp[ci][cj]+1)

print(max(max(row) for row in dp))