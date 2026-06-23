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

기억 상으로는 경로의 최솟값 작게 만드는 거 할 수 있었던 듯 함
근데 경로의 최댓값, 최솟값을 따로 dp로 구하면 같은 경로인지를 알 수 없으니

주어지는 수 범위가 1<= <=100 이니까
최대값이 1이라고 치고 최솟값 최소화 경로를 구하고 ~100까지 반복
근데 최댓값을 설정했다고 해서, 최소 최솟값의 경로에 그 최댓값이 있는 건 아니잖음
최댓값이 뚫리면서 새로운 최솟값 갱신이 되면 확실한데,
최솟값이 똑같은 경우엔 새로 뚫린 최댓값이 진짜 있던건지
기존 최댓값 경로 그대로 나온건지 모르니까

아 아니네 그런거면 최댓값 최솟값 차이의 최소화가 아니겠구나
최댓값 최솟값 차이의 최소화 문제에선 저걸 걱정할 필요가 없음
상한이 증가하고 최솟값이 같으면 차이가 커지니까 어차피 답은 그 전 값임

그럼 최댓값 최솟값 최대화 문제에선
이건 반대로 최솟값을 증가시키면서 최댓값을 dp로 탐색하면 되는건가?

아니지 애초에 최솟값 있는 경로에 실제 최댓값이 존재하는 걸 모르는 게 문제였잖음
그럼 최대 최소를 같이 해? dp 두개?

최솟값을 최대화하기를 해야하는 거였구나
무친 기억력 2주 전 문제조차 기억을 못하죠?
"""
INF = float('inf')

def dp_min(ub):
    dp = [[-1]*N for _ in range(N)]
    dp[0][0] = arr[0][0]
    if dp[0][0] > ub:
        return -1

    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            
            for di, dj in ((1, 0), (0, 1)):
                ni, nj = i+di, j+dj

                if 0<=ni<N and 0<=nj<N and arr[ni][nj] <= ub:
                    dp[ni][nj] = max(min(arr[ni][nj], dp[i][j]), dp[ni][nj])

    if dp[N-1][N-1] == INF:
        return -1
    else:
        return dp[N-1][N-1]

ans = INF
for ub in range(1, 101):
    mn = dp_min(ub)
    if mn == -1:
        continue
    # print('min', mn, 'at', 'ub', ub)
    if ub-mn < ans:
        ans = ub-mn

print(ans)
