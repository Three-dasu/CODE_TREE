N = int(input())
lst = list(map(int, input().split()))
rlst = lst[::-1]

dp_dec = [1]*N
dp_inc = [1]*N

for i, n in enumerate(lst):
    for j in range(i+1, N):
        if rlst[j] > rlst[i]:
            dp_dec[j] = max(dp_dec[j], dp_dec[i]+1)

        if lst[j] > lst[i]:
            dp_inc[j] = max(dp_inc[j], dp_inc[i]+1)
dp_dec = dp_dec[::-1]

ans = 0
for i in range(N):
    
    ans = max(ans, dp_inc[i] + dp_dec[i] - 1)

print(ans)