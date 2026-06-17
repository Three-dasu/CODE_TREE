N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0]-1 for x in clothes]
e = [x[1]-1 for x in clothes]
v = [x[2] for x in clothes]

# 가장 최근 옷 + 날짜 같을 때 화려함 같으면 같음
# dp[i][j] = i일에 j옷 입었을 때 최대 만족도
dp = [[-1]*N for _ in range(M)]
for j in range(N):
    if s[j] <= 0 <= e[j]:
        dp[0][j] = 0


for i in range(1, M):
    for j in range(N):
        for k in range(N):
            if dp[i-1][k] == -1:
                continue

            # 오늘 옷 j를 입는 게 가능하면. k는 이전에 체크 했을테니 따로 조건 필요 x
            if s[j] <= i <= e[j]:
                # 이전 옷과 같음 -> 이 경우를 봐야 하나? -> 봐야지 그 날에 같은 옷만 입을 수 있는 상황도 있으니까   
                if k == j:
                    dp[i][j] = max(dp[i][j], dp[i-1][k])
                else: # 이전 옷과 다름
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(v[k]-v[j]))

# for row in dp:
#     for val in row:
#         print(val, end=' ')
#     print()
# print()

print(max(dp[M-1]))