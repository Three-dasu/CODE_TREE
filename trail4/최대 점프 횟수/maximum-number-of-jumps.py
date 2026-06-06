N = int(input())
lst = list(map(int, input().split()))
dp = [0]*N
v = [0]*N
v[0] = 1

for i in range(N):
    if v[i]:
        for j in range(i+1, i+lst[i]+1):
            if j < N:
                dp[j] = max(dp[i]+1, dp[j])
                v[j] = 1
                # print(dp)

print(max(dp))