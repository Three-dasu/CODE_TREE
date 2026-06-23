N, M = map(int, input().split())
coin = list(map(int, input().split()))

"""
동전 합 M 되는 최소 동전의 수

같은 동전 여러번 사용 가능
합이 같고, 동전 개수가 같으면 같은 상황
합이 같으면 동전 적을수록 좋음

dp[i] = 합이 i인 최소 동전 개수
"""
INF = float('inf')
dp = [INF]*(M+1)
dp[0] = 0   # 합이 0인 최소 동전 개수 0

# 여러번 써야 하니 역순은 안되고
# 그냥 정방향 하면 자동으로 중복 되는 거 아닌가
for n in coin:
    for i in range(M+1):
        if dp[i] == INF:
            continue
        
        if i+n <= M:
            dp[i+n] = min(dp[i+n], dp[i] + 1)


        # k = 1   # 동전 여러개 쓰는 값
        # while n*k <= M or i+n*k <= M:
        #     dp[i+n*k] = dp[i]

        #     k += 1

print(-1 if dp[M]==INF else dp[M])