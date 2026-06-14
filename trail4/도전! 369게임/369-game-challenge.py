import math
N = input()

# 구하려는 것: 박수 몇번 쳐야 하는지

# 같은 상태를 정의하는 요소
# 자리수, 박수 회수, 

L = len(N)

# dp[i][j][k][l] = i번째 자리까지 봤을 때 3으로 나눈 나머지가 j, 369 포함 여부 k, 숫자제한 l
dp = [[[0] * 2 for _ in range(2)] for _ in range(3)]
dp[0][0][1] = 1

MOD = 10**9 + 7

for i in range(L):
    num = int(N[i])
    ndp = [[[0] * 2 for _ in range(2)] for _ in range(3)]
    for j in range(3):
        for k in range(2):
            for l in range(2):
                if dp[j][k][l] == 0:
                    continue
                    
                lim = num if l else 9

                for n in range(lim+1):
                    nj = (j+n) % 3
                    nk = k or (n>0 and n%3 == 0)
                    nl = l and n==lim

                    ndp[nj][nk][nl] = (ndp[nj][nk][nl] + dp[j][k][l]) % MOD
    dp = ndp

ans = 0
for j in range(3):
    for k in range(2):
        for l in range(2):
            if j == 0 or k == 1:
                ans += dp[j][k][l]
                ans = ans % MOD

print((ans+MOD) % MOD -1)

                

