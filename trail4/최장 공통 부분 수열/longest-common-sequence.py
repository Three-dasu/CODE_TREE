A = input()
B = input()

"""
최장 공통 수열 "길이" 찾기.

지금까지 고려한 첫 번째 문자열 위치
지금까지 고려한 두 번째 문자열 위치
지금까지 고려한 공통 부분 수열 최대 길이

dp[i][j]: A를 i까지, B를 j까지 고려했을 때 공통 부분 수열 최대 길이
"""

N_A = len(A)
N_B = len(B)
dp = [[0]*(N_B+1) for _ in range(N_A+1)]

for i in range(N_A+1):
    for j in range(N_B+1):
        
        # A랑 B 다음 문자 같으면 업뎃
        if i < N_A and j < N_B and A[i] == B[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)

        if i < N_A:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        
        if j < N_B:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j])


print(dp[N_A][N_B])