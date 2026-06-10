N = int(input())

dp = [0]*(N+1)
dp[1] = 1
dp[2] = 1
dp[5] = 1
for i in range(N+1):
    for n in (1, 2, 5):
        if i >= n:
            dp[i] += dp[i-n]
print(dp[N] % 10_007)