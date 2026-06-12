def myp():
    for row in dp:
        for val in row:
            print(val, end=' ')
        print()
    print()

N = int(input())
lst = [0]+list(map(int, input().split()))

tot = sum(lst)
if tot%2 == 1:
    print('No')
    exit()

# dp[i][j]: i번째까지 고려했을 때 합 j 만들 수 있냐
dp = [[0]*(tot+1) for _ in range(N+1)]
dp[0][0] = 1

for i, num in enumerate(lst):
    if i == 0:
        continue
    for j in range(tot, -1, -1):
        # 실제로 i번째 숫자를 더하는 경우
        if j-num >= 0 and dp[i-1][j-num] == 1:
            dp[i][j] = 1
        
        # 안더하는 경우
        if dp[i-1][j] == 1:
            dp[i][j] = 1

ans = 'No'
for i in range(N):
    if dp[i][tot//2] == 1:
        ans = 'Yes'
        break

print(ans)