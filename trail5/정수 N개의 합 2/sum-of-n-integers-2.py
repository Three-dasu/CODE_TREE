N, K = map(int, input().split())
lst = list(map(int, input().split()))


prefix_sum = [0] * (N+1)

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + lst[i-1]

ans = -2**31
for i in range(N+1-K):
    tmp = prefix_sum[i+K] - prefix_sum[i]
    if tmp > ans:
        ans = tmp

# print(prefix_sum)
print(ans)