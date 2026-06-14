N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 같은 상태를 정의하는 요소
# 위치, 구간, 합

# 숫자를 뺀다고 생각하면 되지 않을까
# M개 구간이 필요하면 M-1개의 숫자를 빼면 되는거지
# 대신 빼는 숫자들은 직전에 뺀 경우엔 이어서 빼면 한덩이로 치고
# 그럼 처음숫자를 빼는 경우는?

# 그냥 이전엔 안뺐는데 이번엔 뺀다 -> 구간 1개 생성 일케 보는 게 나을듯
# dp 배열에도 그냥 M개 구간으로 놓고

INT_MIN = -2**31
# dp[i][j][k]: i번째 숫자까지, j개 구간일 때, i-1번째 숫자를 뺐으면 k=0 아니면 k=1 에서 최대 합
dp = [[[INT_MIN]*2 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(M+1):
        for k in range(2):
            if dp[i][j][k] == INT_MIN:
                continue

            # i번째 숫자를 구간에 포함
            if k == 0:      # i-1번째 숫자를 뺀 상태면 (k==0) 새로운 구간 시작
                if j < M:
                    dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][k] + lst[i])
            else:           # i-1번째 숫자가 포함된 상태면 구간 이어짐
                dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][k] + lst[i])

            # i번째 숫자 제외
            if k == 0:      # i-1번째 숫자를 뺀 상태면 (k==0) 빼는 게 이어짐
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][k])
            else:           # i-1번째 숫자가 포함된 상태면 구간 이어짐
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][k])

# for row in dp:
#     for val in row:
#         print(f'{val[0]:>2}', end=' ')
#     print()
# print()

# for row in dp:
#     for val in row:
#         print(f'{val[1]:>2}', end=' ')
#     print()
# print()


print(max(max(row[M]) for row in dp))