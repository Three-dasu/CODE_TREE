N = int(input())
treasure = []

for i in range(N):
    l, m, r = map(int, input().split())
    treasure.append((l, m, r))

# 전 문제랑 같지만, 1층 방을 상태로 추가해야 함
dp = [[[0]*3 for _ in range(3)] for _ in range(N)]
for j in range(3):
    dp[0][j][j] = treasure[0][j]


for i in range(N-1):              # 현재 층
    for j in range(3):          # 현재 층 방
        for k in range(3):      # 첫번째 층 방
            if dp[i][j][k] == 0:
                continue
            
            for l in range(3):  # 다음 층 방
                if j == l or (i==N-2 and l==k):
                    continue
                dp[i+1][l][k] = max(dp[i+1][l][k], dp[i][j][k] + treasure[i+1][l])

print(max(max(row) for row in dp[N-1]))
