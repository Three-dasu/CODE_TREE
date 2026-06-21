N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

"""


dp[i][j] = A의 i까지, B의 j 까지 봤을 때 공통 부분 수열의 최대 길이
"""

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(N, -1, -1):
    for j in range(M, -1, -1):
        
        if i>0 and j>0 and a[i-1] == b[j-1]:
            dp[i-1][j-1] = max(dp[i-1][j-1], dp[i][j] + 1)
        
        # push에서 조건 달기가 좀 애매하네 a[i] != b[j]를 어따 넣어야 하는거야
        if i>0:
            dp[i-1][j] = max(dp[i-1][j], dp[i][j])
        if j>0:
            dp[i][j-1] = max(dp[i][j-1], dp[i][j])

# for row in dp:
#     for val in row:
#         print(val, end=' ')
#     print()
# print()

nxt_A = [[N]*1001 for _ in range(N+1)]
nxt_B = [[M]*1001 for _ in range(M+1)]

last_A = [N]*1001
for i in range(N-1, -1, -1):
    last_A[a[i]] = i
    nxt_A[i] = last_A[:]

last_B = [M]*1001
for j in range(M-1, -1, -1):
    last_B[b[j]] = j
    nxt_B[j] = last_B[:]

commons = sorted(list(set(a) & set(b)))

# 역추적
ln = dp[0][0]
i, j = 0, 0
ans = []

while ln > 0:
    for x in commons:
        ni = nxt_A[i][x]
        nj = nxt_B[j][x]

        # i, j번째에서 최초로 나오는 x값이 N, M 보다 작아야 존재한다는 거니까 그걸로 필터링
        # ni, nj 확인하고 둘 다 하나씩 더 갔을 때 dp값에 변화가 생기면 -> 그 부분에서 공통 문자가 생겼구나
        if ni<N and nj<M and dp[ni+1][nj+1] == ln - 1:
            i, j = ni+1, nj+1
            ans.append(x)
            ln -= 1
            break

print(*ans)