N = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(N)]


dp = [0]*N
for i in range(N):
    s, e, p = jobs[i]
    dp[i] = p


for i in range(N):
    s, e, p = jobs[i]

    for j in range(i+1, N):
        ns, ne, np = jobs[j]

        if e < ns:
            dp[j] = max(dp[j], dp[i] + np)


print(max(dp))