N = int(input())
s = []
b = []
for _ in range(N):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

def myp():
    for row in dp:
        for val in row:
            print(val, end=' ')
        print()
    print()

# 구하는 것: 20명 능력 합의 최대
# 요소: 고려한 사람, 축구합, 야구합, 총합
# dp[i][j][k] = 사람 i명 고려했을 떄, 축구 j, 야구 k명 채운 상황에서 능력치 합의 최댓값
# dp[j][k] = 굳이 사람 i명 따질 필요 없을 듯. 축구 j, 야구 k명 채운 상황에서 능력치 합의 최댓값
J, K = 11, 9    # 채워야 하는 사람 수

dp = [[-1]*(K+1) for _ in range(J+1)]
dp[0][0] = 0


for i in range(N):
    for j in range(J, -1, -1):
        for k in range(K, -1, -1):
            # if j + k > i:
            #     continue
            # if dp[j][k] == -1:
            #     continue

            # # 축구 인원 여유 축구에 배정
            # if j < J:
            #     dp[j][k] = max(dp[j][k], dp[j-1][k] + s[i])

            # 기존 축구 한명 빼고 축구 새 사람 추가
            if j > 0 and dp[j-1][k] != -1:
                dp[j][k] = max(dp[j][k], dp[j-1][k] + s[i])

            # # 야구 인원 여유 야구에 배정
            # if k < K:
            #     dp[j][k+1] = max(dp[j][k+1], dp[j][k] + b[i])
            
            # 기존 야구 한명 빼고 새 사람 추가
            if k > 0 and dp[j][k-1] != -1:
                dp[j][k] = max(dp[j][k], dp[j][k-1] + b[i])

    # myp(1)
print(dp[J][K])