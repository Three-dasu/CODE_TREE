N, M = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i]: 시간 i에서 최대 경험치 값
dp = {}
dp[0] = 0

for e, t in quests:
    ndp = dp.copy()
    for i in dp:
        if i+t not in dp:
            ndp[i+t] = dp[i] + e
        else:
            ndp[i+t] = max(dp[i+t], dp[i] + e)

    dp = ndp

ans = 2**31
for k, v in dp.items():
    if v >= M and k < ans:
        ans = k

if ans == 2**31:
    print(-1)
else:
    print(ans)