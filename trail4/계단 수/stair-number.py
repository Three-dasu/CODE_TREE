N = int(input())

"""
길이가 N인 인접한 수의 차이가 모두 1인 수의 개수 구하기
요소: 길이 / 마지막 숫자 / 개수
dp[i][j] = 길이 i+1, 마지막 숫자가 j 인 계단 수의 개수
"""
MOD = 10**9 + 7
dp = [[0]*10 for _ in range(N)]
for j in range(1, 10):
    dp[0][j] = 1

for i in range(1, N):
    for j in range(10):
        # 직전 숫자 k
        for k in (j-1, j+1):
            if k<0 or k>=10 or dp[i-1][k] == 0:
                continue

            dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

print(sum(dp[N-1]) % MOD)