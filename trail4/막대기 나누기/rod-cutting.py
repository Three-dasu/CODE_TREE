N = int(input())
profit = list(map(int, input().split()))

# dp[i]: 길이합 i의 막대를 팔았을 때의 최대 수익...?
dp = [-1]*(N+1)
dp[0] = 0

for i in range(N+1):
    for j, p in enumerate(profit):
        if i>=j+1 and i-j-1 != -1:
            dp[i] = max(dp[i], dp[i-j-1]+p)
    # print(dp)
print(max(dp))