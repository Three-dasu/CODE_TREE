N = int(input())
lst = list(map(int, input().split()))

"""
A합과 B합이 같게, 대신 그 합이 최대가 되게끔

A와 B의 차이가 같고, A합이 같으면 같은 상황이지 않은가
그럼 A와 B의 차이에서 A합을 최대화 하는 걸로 하면
dp[0]하면 되는 거 아닐까

dp[i] = A와 B의 차이 i 에서 무거운 쪽의 합 최댓값
"""

tot = sum(lst)
dp = [-1] * (tot+1)
dp[0] = 0

for w in lst:
    ndp = dp[:]
    for i in range(tot, -1, -1):
        if dp[i] == -1:
            continue
        
        # 무거운 쪽에 넣기
        nw = i + w
        if nw <= tot:
            ndp[nw] = max(ndp[nw], dp[i] + w)
        
        # 가벼운 쪽에 넣기
        cw = dp[i] - i  # 현재 무게 = 무거운 쪽 - 차이
        nw = cw + w

        # 가벼운 쪽에 넣었지만 여전히 가볍다면
        if nw < dp[i]:
            ndp[dp[i]-nw] = max(ndp[dp[i]-nw], dp[i])
        # 가벼운 쪽에 넣어서 무거워졌다면
        else:
            ndp[nw-dp[i]] = max(ndp[nw-dp[i]], nw)

        # # 버리기
        # nw = i
        # dp[i] = max(dp[i], dp[i] + w)
    # print(ndp)
    dp = ndp

print(dp[0])