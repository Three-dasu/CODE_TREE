s = input()
t = input()
N, M = len(s), len(t)

"""
두 문자열의 상위수열 중 가장 짧은 문자열 길이 구하기

앞에서 LCS 풀 때는 최장 공통 부분 수열을 찾는거다 보니까 max를 했었는데, 이 문제는 가장 짧은 상위 수열을 찾는 것
어쨌든 이 문제도 LCS 구하고 각 문자열 길이를 더하고 LCS 한번만 빼는 식으로 구할 수는 있을 거 같은데
이건 다음 두 문자열의 문자가 다른 경우에도 두 문자열 중 하나씩 더 보면서 길이를 추가하는데,
그 전 LCS문제들은 그냥 그대로 가져왔었음
그치만 min 사용해서 이렇게 풀어도 상관 없지 않을까

얼핏 생각하면 그냥 둘 다 하나씩 증가시키면서 다른 경우엔 길이 2를 추가해도 되지 않을까 싶지만
이건 다른 위치에서 겹치는 경우 (i=3 j=5 위치 등)를 생각하지 않으니까 이렇게 푸는 게 맞겠지?

dp[i][j]: s를 i까지, t를 j까지 봤을 때 상위수열 최단길이
"""
INF = float('inf')

dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(M+1):
        if dp[i][j] == INF:
            continue

        # 같은 경우엔 둘 다 하나씩 더 보고 길이 1 추가
        if i<N and j<M and s[i]==t[j]:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + 1)
        else:
            # 다른 경우, i만 하나 더 보고 그 전 값에서 문자 하나 추가 (길이 +1)
            if i<N:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)

            # 다른 경우, j만 하나 더 보고 그 전 값에서 문자 하나 추가 (길이 + 1)
            if j<M:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)

# for row in dp:
#     for val in row:
#         print(val, end=' ')
#     print()
# print()

print(dp[N][M])