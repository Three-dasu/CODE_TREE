N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort(lambda x: (x[1]))
dp = [1]*N

for i, (a1, b1) in enumerate(lst):
    
    for j in range(i):
        a2, b2 = lst[j]
        if b2 < a1:
            dp[i] = max(dp[j]+1, dp[i])
    
print(max(dp))
