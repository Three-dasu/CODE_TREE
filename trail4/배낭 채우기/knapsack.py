N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# dp[i]: 무게 i에서 가치의 최댓값
dp = [-1] * (M+1)
dp[0] = 0

for j in range(N):
    for i in range(M, -1, -1):
        if i >= w[j] and i-w[j] != -1:
            dp[i] = max(dp[i], dp[i-w[j]] + v[j])

print(max(dp))