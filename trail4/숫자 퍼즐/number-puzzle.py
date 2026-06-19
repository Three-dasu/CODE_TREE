N, M, K = map(int, input().split())

"""
0은 제외인가
아무리 봐도 백트래킹이 맞는데
이게 왜 dp야
어차피 for 탐색은 사전순일테니 조건에 맞으면 t를 1씩 증가시키는 걸로 하고

고려한 숫자 개수, 새겨진 숫자의 합, 마지막 숫자

첫자리부터 숫자를 오름차순으로 하나씩 넣어보면서
해당 숫자에서 나올 수 있는 수열이 몇개인가 cnt
1. cnt > K: 이번 수열 안에 K번쨰가 있겠구나
2. cnt == K: 이거다
1, 2를 묶어서 다뤄야 할 듯
3. cnt < K: 이 숫자 말고 다음 숫자로 넘어가기 (대신 K는 cnt만큼 차감)
뫈반복

dp[i][j][k]: i번째 자리에 숫자 j이고 현재 합이 m일 때 가능한 수열의 경우의 수
"""

dp = [[[0]*(M+1) for _ in range(M+1)] for _ in range(N+1)]
for j in range(1, M+1):
    dp[N][j][M] = 1

for i in range(N, 0, -1):
    for j in range(1, M+1):
        for m in range(M+1):
            if m-j < 0 or dp[i][j][m] == 0:
                continue

            for nj in range(1, j+1):
                dp[i-1][nj][m-j] += dp[i][j][m]
        

lst = []
curr_sum = 0
last_n = 1

for i in range(1, N+1): # 첫번째 자리부터 N번째 자리까지 하나씩 탐색

    for n in range(last_n, M+1):
        if curr_sum + n > M:
            break
        
        cnt = dp[i][n][curr_sum+n]
        if cnt >= K:
            curr_sum += n
            last_n = n
            lst.append(n)
            break

        else:
            K -= cnt

print(*lst)
