A = input()
B = input()
N, M = len(A), len(B)

"""
최장 공통 부분 수열을 찾아서, 출력까지 해야함

dp로 길이를 구하고 그 길이로 백트래킹 하는건가?
아니면 dp 배열에서 정보를 얻어서?
일단 길이부터 찾자

탐색한 A의 위치, B의 위치, 최장 공통 부분 수열 길이가 같으면 같다.
dp[i][j]: A를 i까지, B를 j까지 봤을 때 최장 공통 부분 수열의 길이
"""
dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):

        # 같은 경우
        if A[i-1] == B[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

        # 다른 경우
        else:
            # dp[i-1][j]: B만 하나 더 본거, dp[i][j-1]: A만 하나 더 본거
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

# for row in dp:
#     for val in row:
#         print(val, end=' ')
#     print()
# print()

# print(dp[N][M])
"""
(1,1) 부터 (N, M)까지 탐색. 방향은 (1, 1) 먼저 쭉 가고
끝에 갔는데 최장 공통 부분수열 길이 안나왔으면 (0, 1), (1, 0) 중에 가능한 방향으로
탐색하면서 숫자가 늘어나면 그 인덱스 기록 나중에 그거 보면서 부분 수열 재구성
ex)
(1, 1) 시작점에서 dp값 1
(4, 4) 에서 dp값 2
(4, 5) 에서 dp값 3

pa, pb를 1, 1로 초기화 하고
dp값 상승 배열 첫번째 (1, 1) 이걸 각각 ta, tb 로 하고
A[pa:ta+1] 먼저 돌면서 set으로 만들고 B[pb:tb+1] 돌면서 set에 있나 확인. 무조건 있을테니 그 글자를 정답에 추가
pa, pb를 ta, tb로 업데이트
다음 dp값 상승이 있었던 (4,4)로 다시 반복
A[pa:ta+1] 먼저 돌면서 set으로 만들고 B[pb:tb+1] 돌면서 set에 있나 확인. 무조건 있을테니 그 글자를 정답에 추가

이럴 경우 시간 복잡도는 N씩 두번이니까 N
set 만드는 비용 시간은 어케 되는거지

set도 그렇고 탐색도 그렇고 문제가 많네 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
"""
i, j = N, M
ans = ""
while i>0 and j>0:
    if A[i-1] == B[j-1]:
        ans += A[i-1]
        i -= 1
        j -= 1
    
    else:
        if dp[i-1][j] <= dp[i][j-1]:
            j -= 1
        else:
            i -= 1

print(ans[::-1])
