def myp():
    for row in dp:
        for val in row:
            print(f'{val:>2}', end=' ')
        print()
    print()

N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

# dp[i]: i번째 턴에서 남우 점수 최댓값
# dp[i]: 남우가 i번째 카드까지 썼을 때의 최댓값

# 근데 어쨌든 최댓값을 구하려면 둘 모두 카드를 어디까지 썼는지 알아야할 것 같긴 함
# 남은 게 없으면 그때 끝내야 할 거 아녀

# dp[i][j]: A가 i번째 카드, 남우가 j번째 카드까지 썼을 때의 최댓값

dp = [[-1] * (N + 2) for _ in range(N + 2)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(N+1):
        if dp[i][j] == -1:
            continue

        # print(i, j)
        # print(A[i], B[j])

        # [1] 카드 대결
        # [1-1] A < B
        if A[i] < B[j]:
            # print(i, j)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

        # [1-2] A > B
        elif A[i] > B[j]:
            # print(i, j)
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + B[j])

        # [1-3] A == B
        else:
            # print(i, j)
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

        # [2] 버리기
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])


        # myp()

print(max(max(row) for row in dp))