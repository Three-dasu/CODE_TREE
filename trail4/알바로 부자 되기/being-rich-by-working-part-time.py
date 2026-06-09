N = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(N)]


dp = [0]*N
for i in range(N):
    s, e, p = jobs[i]
    dp[i] = p


for i in range(N):
    s, e, p = jobs[i]

    for j in range(i):
        ps, pe, pp = jobs[j]

        if pe < s:
            dp[i] = max(dp[i], dp[j] + p)


print(max(dp))