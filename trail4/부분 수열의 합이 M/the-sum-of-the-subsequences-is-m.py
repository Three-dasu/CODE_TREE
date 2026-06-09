N, M = map(int, input().split())
A = list(map(int, input().split()))

# dp:합이 dp[i]인 최소 수열의 길이
dp = [N+1] * (M+1)

dp[0] = 0
for j in A:
    # print(j, 'turn')
    for i in range(M, -1, -1):
        if i >= j:
            # print('update', i, 'comparing', dp[i], 'and', dp[i-j])
            dp[i] = min(dp[i], dp[i-j]+1)

    # print(dp)


if dp[M] == N+1:
    print(-1)
else:
    print(dp[M])