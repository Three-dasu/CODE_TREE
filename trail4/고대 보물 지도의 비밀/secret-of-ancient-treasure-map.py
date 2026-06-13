def myp():
    for row in dp:
        for val in row:
            print(f'{val:>2}', end=' ')
        print()
    print()

N, K = map(int, input().split())
lst = list(map(int, input().split()))

# dp[i][j]: i번째 수까지 봤을 때 음수가 j개인 최대합
dp = [[-2**31]*(K+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(K+1):
        # if dp[i][j] == -2**31:
        #     continue
        
        # [1] 이번 숫자 선택 or 새로 시작
        if lst[i] > 0:      # 양수
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+lst[i])
            dp[i+1][0] = max(dp[i+1][0], lst[i])
        else:               # 음수
            if j == K:
                continue
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+lst[i])
            dp[i+1][1] = max(dp[i+1][1], lst[i])

        # myp()

# 모두 음수라서 dp[0][0], 즉 0이 최대인 경우도 생각해야 함
dp[0][0] = -2**31
print(max(max(row) for row in dp))