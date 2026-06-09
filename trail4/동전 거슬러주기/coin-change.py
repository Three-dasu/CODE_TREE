N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp = [10**9] * (M+1)


dp[0] = 0

for i in range(M+1):
    for n in coin:
        if i >= n:
            dp[i] = min(dp[i], dp[i-n] + 1)
    
    # print(dp)

if dp[M] == 10**9:
    print(-1)
else:
    print(dp[M])