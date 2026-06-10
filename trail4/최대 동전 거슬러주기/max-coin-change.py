N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp = [0] + [-1]*M

for i in range(M+1):
    for n in coin:
        if i>=n and dp[i-n] != -1:
            dp[i] = max(dp[i], dp[i-n]+1)

print(dp[M])
