N = int(input())
s = []
b = []
for _ in range(N):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

# 구하는 것: 20명 능력 합의 최대
# 요소: 고려한 사람, 축구합, 야구합, 총합
# dp[i][j][k] = 사람 i명 고려했을 떄, 축구 j, 야구 k명 채운 상황에서 능력치 합의 최댓값
dp = [[[0]*(10) for _ in range(12)] for _ in range(N+1)]
dp[0][0][0] = 0


"""
근데 새로운 사람을 고려할 때 20명이 다 찬 상태면 기존 인원을 빼고 넣어야 하잖아
그럼 그냥 한명씩 보면서 하면 되는 거 아닌가
1000x20
"""

for i in range(N):
    for j in range(12):
        for k in range(10):
            if j + k > i:
                continue

            # 안넣는 경우
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

            if j < 11:
                dp[i+1][j+1][k] = max(dp[i+1][j+1][k], dp[i][j][k] + s[i])
            
            if k < 9:
                dp[i+1][j][k+1] = max(dp[i+1][j][k+1], dp[i][j][k] + b[i])

# def myp(n):
#     for row in dp[n]:
#         for val in row:
#             print(val, end=' ')
#         print()
#     print()

# myp(1)
print(dp[N][11][9])
