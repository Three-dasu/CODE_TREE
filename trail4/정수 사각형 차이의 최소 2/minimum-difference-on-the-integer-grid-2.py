N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def myp():
    for row in dp:
        for val in row:
            if val==INF:
                print(0, end=' ')
            else:
                print(val, end=' ')
        print()
    print()

"""
경로 상 최댓값과 최솟값의 차이 작게 만들기
(1<=N<=100, 1<=주어지는 수<=100)

3차원 dp로 풀어봅시다
dp[i][j][k] = i, j 까지 갈 때 최솟값 k로 얻을 수 있는 최댓값
"""
INF = float('inf')
dp = [[[INF]*101 for _ in range(N)] for _ in range(N)]
dp[0][0][arr[0][0]] = arr[0][0]

for i in range(N):
    for j in range(N):
        for k in range(101):
            if dp[i][j][k] == INF:
                continue
            
            for di, dj in ((1, 0), (0, 1)):
                ni, nj = i+di, j+dj

                if 0<=ni<N and 0<=nj<N:
                    # 기존 최소는 k
                    nk = min(k, arr[ni][nj])
                    # 최대 업뎃
                    dp[ni][nj][nk] = min(dp[ni][nj][nk], max(dp[i][j][k], arr[ni][nj]))

ans = float('inf')
for k in range(101):
    if dp[N-1][N-1][k] == INF:
        continue
    val = dp[N-1][N-1][k] - k
    if val < ans:
        ans = val
# print([(k, x) for k, x in enumerate(dp[N-1][N-1]) if x<1000])
print(ans)
