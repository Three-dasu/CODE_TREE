N = int(input())
lst = list(map(int, input().split()))
# lst.sort()

# 4
# 2 2 1 5

tot = sum(lst)
dp = [2**31] * (tot)
dp[0] = -tot

for n in lst:
    for i in range(tot-1, 0, -1):
        if i>=n:
            dp[i] = min(dp[i], dp[i-n] + 2*n)

dp = [abs(x) for x in dp]
print(min(dp))