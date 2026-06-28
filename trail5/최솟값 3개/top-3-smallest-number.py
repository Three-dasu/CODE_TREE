N = int(input())
lst = list(map(int, input().split()))

# 가장 작은 숫자 3개의 곱 출력하기
# hq 특성: 인덱스 0이 최소, 1, 2가 0의 자식 노드 3, 4가 1의 자식 노드 5, 6이 2의 자식 노드
# 근데 1이 5, 6보다 작은것도 보장이 되나 되겠지 뭐
# 안되나봄 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# 그럼 매번 꺼내야 해? 개귀찮

import heapq as hf
hq = []

for n in lst:
    hf.heappush(hq, n)

    if len(hq)<3:
        print(-1)
        continue
    
    ans = 1
    tmp = []
    for _ in range(3):
        x = hf.heappop(hq)
        ans *= x
        tmp.append(x)
        
    for i in range(3):
        hf.heappush(hq, tmp[i])

    print(ans)