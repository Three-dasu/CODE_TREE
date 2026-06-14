N = int(input())

# 특정 시점에서 t의 개수와 연속한 b의 개수가 같으면 같음
# dp[i][j][k]: i번째 날에 받은 j개의 B와 k개의 T로 살아남은 경우의 수
# 이진수로 한다면...?! 차이가 없는데 말만 2차원이지 배열 요소 개수는 똑같

dp = [[0]*3 for _ in range(3)]
dp[0][0] = 1

for i in range(N):
    ndp = [[0]*3 for _ in range(3)]

    for j in range(3):
        for k in range(3):

            # G: B 개수 초기화
            ndp[0][k] += dp[j][k] % (10**9 + 7)

            # B
            if j < 2:
                ndp[j+1][k] += dp[j][k] % (10**9 + 7)

            # T: B 개수 초기화
            if k < 2:
                ndp[0][k+1] += dp[j][k] % (10**9 + 7)

    dp = ndp


print(sum(sum(row) for row in dp) % (10**9 + 7))