N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [-1] * (M+1)
dp[0] = 0

for n in A:
    for i in range(M, -1, -1):
        if i>=n and dp[i-n] != -1:
            dp[i] = max(dp[i], dp[i-n]+1)

if dp[M]>0:
    print('Yes')
else:
    print('No')