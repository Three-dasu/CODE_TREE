N, K = map(int, input().split())
str = list(input())
crystal = [0]
for n in range(N):
    c = 0 if str[n] == 'L' else 1
    crystal.append(c)

# 턴, 위치, 이동 -> 최대 수정 개수
dp = [[[-1]*(K+1) for _ in range(2)] for _ in range(N+1)]
# 출발 위치 왼쪽 고정

# 첫 수정이 왼쪽이면 1 아니면 0
dp[1][0][0] = 1 if crystal[1] == 0 else 0
# 이동을 처음에 할 수도 있나봄
dp[1][1][1] = 1 if crystal[1] == 1 else 0

for i in range(1, N):
    for j in range(2):
        for k in range(K+1):
            if dp[i][j][k] == -1:
                continue
            
            # 안움직임
            nj = j
            dp[i+1][nj][k] = max(dp[i+1][nj][k], dp[i][j][k] + (crystal[i+1]==nj))

            # 움직임
            if k < K:
                nj = 1- j
                dp[i+1][nj][k+1] = max(dp[i+1][nj][k+1], dp[i][j][k] + (crystal[i+1]==nj))

print(max(max(row) for row in dp[N]))