N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
prefix = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + arr[i-1][j-1]

ans = 0
for i in range(N+1-K):
    for j in range(N+1-K):
        tmp = prefix[i+K][j+K] - prefix[i][j+K] - prefix[i+K][j] + prefix[i][j]
        if tmp > ans:
            ans = tmp

print(ans)