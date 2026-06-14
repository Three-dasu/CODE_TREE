N = int(input())

# 특정 시점에서 t의 개수와 연속한 b의 개수가 같으면 같음
# dp[i][j][k]: i번째 날에 받은 j개의 B와 k개의 T로 살아남은 경우의 수
dp = [[[0]*3 for _ in range(3)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    ndp = [[[0]*3 for _ in range(3)] for _ in range(N+1)]

    for j in range(3):
        for k in range(3):

            # G: B 개수 초기화
            ndp[i+1][0][k] += dp[i][j][k]

            # B
            if j < 2:
                ndp[i+1][j+1][k] += dp[i][j][k]

            # T: B 개수 초기화
            if k < 2:
                ndp[i+1][0][k+1] += dp[i][j][k]

    dp = ndp

    # for row in dp:
    #     for val in row:
    #         print(val, end=' ')
    #     print()
    # print()

print(sum(sum(row) for row in dp[N]) % (10**9 + 7))