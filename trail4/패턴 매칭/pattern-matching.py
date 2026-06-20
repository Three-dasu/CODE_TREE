s = input()
P = input()


p = []
i=0
while i < len(P):
    if i<len(P)-1 and P[i+1] == '*':
        p.append(P[i:i+2])
        i += 2
    
    else:
        p.append(P[i])
        i += 1

N = len(s)
M = len(p)
s = ' ' + s
p = [' '] + p


"""
s가 p에 속하는지 판단
이걸 도대체 왜 dp로 해야하지

s의 i까지가 p의 j까지에 속하는지를 보면 될 듯
대신 p를 좀 잘 나눠야 할 거 같은데
알파벳만 하나 있으면 그거 한덩어리
. 하나만 있으면 이것도 한덩어리
뒤에 *이 붙으면 이게 바로 두개가 한덩어리 ex) a* .*
p를 전처리를 좀 해서 의미단위로 나눠야 하지 않을까

p의 j번째가 a*인 경우 -> s의 i번째 기준으로

1. a가 아니면 0개라고 치고 그냥 넘어가기
2. a면 a 아닌게 될 때까지 i 쭉 증가시키면서 기존값 대입 -> 이거때문에라도 push로...?

dp[i][j] = s의 i까지가 p의 j까지에 속하는지 여부
"""

dp = [[0]*(M+2) for _ in range(N+2)]
dp[0][0] = 1

# 굳이 초기화 필요 없는 문제인 듯
# for i in range(1, N+1):
#     dp[i][0] = 0
# for j in range(1, M+1):
#     dp[0][j] = 0

for i in range(N+1):
    for j in range(M+1):  # j확인하게 되면서 또 여기가 재랄이 나는구나.... 기존에 M이었으니 M+1로 고쳐야지...
        if dp[i][j] == 0:
            continue
        
        if j < M:
            if len(p[j+1]) == 1:
                if i < N:
                    if p[j+1] == '.' or p[j+1] == s[i+1]:
                        dp[i+1][j+1] = 1
                    else:
                        # 여기 max는 왜 안써도 되는거야 dp[i+1][j+1]이 1일 수도 있잖어
                        dp[i+1][j+1] = max(dp[i+1][j+1], 0)

            else:   # * 달린 경우
                # 없다 치고 p 하나 넘어가기
                # dp[i][j] 0일때 continue 해놓고 max를 왜하는 건데. 그치만 기억하기 위해 냅두자
                dp[i][j+1] = max(dp[i][j+1], dp[i][j])

        if len(p[j])==2:    # 와 밑에 바꾸려면 p[j]로 확인해줘야 하네.....
            # 둘이 똑같음 or 무적의 . 케이스 끝까지 쭉 true로 밀기
            if i < N and (p[j][0] == s[i+1] or p[j][0] == '.'):
                dp[i+1][j] = 1

                # 다르면 그냥 없다치고 넘어가면 되니까 필요 없을 듯 주석처리
                # else:
                #     dp[i+1][j+1] = max(dp[i+1][j+1], 0)

# for row in dp:
#     for val in row:
#         print(val, end=' ')
#     print()
# print()

print('true' if dp[N][M]==1 else 'false')

