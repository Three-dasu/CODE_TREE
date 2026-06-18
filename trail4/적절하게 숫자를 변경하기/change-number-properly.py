N, M = map(int, input().split())
lst = [0] + list(map(int, input().split()))
lst = [x-1 for x in lst]

# 비슷한 수열 중에 유사도 젤 높은 거 찾기
# 고려한 길이 같을 때, 비슷함 정도는 이하면서, 마지막 숫자도 같은데, 유샤도가 최대인
dp = [[[-1]*(4) for _ in range(M+1)] for _ in range(N+1)]
for k in range(4):
    dp[1][0][k] = 1 if k == lst[1] else 0 

for i in range(1, N):
    for j in range(M+1):
        for k in range(4):      # 현재 숫자 k
            if dp[i][j][k] == -1:
                continue

            for l in range(4):  # 다음 숫자 l
                val = (lst[i+1] == l)
                # 같은 숫자
                if k == l:
                    dp[i+1][j][l] = max(dp[i+1][j][l], dp[i][j][k] + val)
                
                elif j<M:
                    dp[i+1][j+1][l] = max(dp[i+1][j+1][l], dp[i][j][k] + val)

print(max(max(row) for row in dp[N]))


