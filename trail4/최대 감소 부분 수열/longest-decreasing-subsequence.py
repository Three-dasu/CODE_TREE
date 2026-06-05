N = int(input())
lst = [10001] + list(map(int, input().split()))
M = len(lst)

# i위치까지 감소 부분 수열의 최대 길이
dp = [0] + [-1] * M

for i in range(1, N+1):
    for j in range(i):
        if lst[j] > lst[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))