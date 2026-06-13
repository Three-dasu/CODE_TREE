N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 똑같은 상태를 정의하는 요소 찾기
# 지금 문제는 합이 같으면 그 이후 계산에서 취하는 행동이 같은 결과를 보임
# 합으로 dp

# dp[i]: 계산했을 때 합이 i가 되는 가짓수
dp = {}
cnt = 0

if lst[0] == 0:
    dp[0] = 2
else:
    dp[lst[0]] = 1
    dp[-lst[0]] = 1


for n, num in enumerate(lst):
    ndp = {}
    
    if n == 0:
        continue
    
    # 0 하나마다 경우의 수 2배씩 늘어나니까 미리 세두고
    if num == 0:
        cnt += 1
        continue

    for k in dp:

        if -20 <= k+num <= 20:
            if k+num in ndp:
                ndp[k+num] += dp[k]
            else:
                ndp[k+num] = dp[k]
        
        if -20 <= k-num <= 20:
            if k-num in ndp:
                ndp[k-num] += dp[k]
            else:
                ndp[k-num] = dp[k]
    
    dp = ndp

if M in dp:
    print(dp[M] * (2**cnt))
else:
    print(0)