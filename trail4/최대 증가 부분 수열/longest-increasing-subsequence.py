N = int(input())
lst = list(map(int, input().split()))
dp = [1]*(len(lst))
dp[0] = 1

for i, n in enumerate(lst):
    
    for j in range(i+1, len(lst)):
        if lst[j] > n:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))