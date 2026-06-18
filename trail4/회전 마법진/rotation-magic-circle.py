N = int(input())
a = input()
b = input()

"""
최소 회전 수
반시계 회전 수

dp[i][j] = i번째 마법진 / j번의 반시계 회전 / 최소 회전 수
"""
dp = [[2**31]*10 for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(10):
        if dp[i][j] == 2**31:
            continue

        num = int(a[i])+j
        if num >= 10:
            num -= 10

        diff = num - int(b[i])


        # print(i, j, 'from', a[i], 'to', num, 'to', b[i])

        if diff < 0:
            ccw, cw = abs(diff), 10+diff
        elif diff > 0:
            ccw, cw = 10-diff, diff
        else:
            ccw, cw = 0, 0
        
        # print('ccw:', ccw, 'cw:', cw)

        # 반시계
        nj = j + ccw
        if nj > 9:
            nj = nj-10
        dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + ccw)
        
        # 시계
        dp[i+1][j] = min(dp[i+1][j], dp[i][j] + cw)

# for row in dp:
#     for val in row:
#         if val == 2**31:
#             val = -1
#         print(f'{val:>2}', end=' ')
#     print()
# print()

print(min(dp[N]))