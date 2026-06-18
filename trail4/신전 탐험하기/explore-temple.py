N = int(input())
v = [[], [], []]
for _ in range(N):
    left, mid, right = map(int, input().split())
    v[0].append(left)
    v[1].append(mid)
    v[2].append(right)

# 매 층마다 다른 방 들어가며 최대 보물
# 층, 들어간 방, 보물
# dp[i][j]: i층의 j번째 방까지 들어갔을 떄 최대 보물
dp = [[0]*3 for _ in range(N)]
dp[0] = [v[0][0], v[1][0], v[2][0]]

for i in range(N-1):
    for j in range(3):
        if dp[i][j] == 0:
            print('skiip')
            continue
        # i+1층 방 탐색
        for k in range(3):
            if j == k:
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j]+v[k][i+1])

print(max(dp[N-1]))