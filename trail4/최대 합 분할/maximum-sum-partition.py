N = int(input())
lst = list(map(int, input().split()))

tot = sum(lst)
# dp[i]: 차이가 i인 조합의 큰 부분 합
dp = [-1] * (tot + 1)
dp[0] = 0

for n, num in enumerate(lst):
    ndp = dp[:]
    for i in range(tot, -1, -1):
        if dp[i] != -1:
            
            # 큰 쪽 = dp[i]
            # 작은 쪽 = dp[i] - i

            # 작은 쪽에 더하기
            new_diff = abs(i - num)
            ndp[new_diff] = max(ndp[new_diff], dp[i]-i + num, dp[i])

            # 큰 쪽에 더하기
            new_diff = i + num
            ndp[new_diff] = max(ndp[new_diff], dp[i] + num)
    dp = ndp

print(dp[0])