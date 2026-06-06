N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort(lambda x: (x[1]))
dp = [1]*N

for i, (a1, b1) in enumerate(lst):
    
    for j in range(i+1, N):
        a2, b2 = lst[j]
        if a2 > b1:
            dp[j] = max(dp[i]+1, dp[j])
    
print(max(dp))
