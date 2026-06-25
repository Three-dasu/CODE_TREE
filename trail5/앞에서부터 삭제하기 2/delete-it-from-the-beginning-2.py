N = int(input())
lst = list(map(int, input().split()))

import heapq as hg

"""
1. 앞에서 K개 삭제
2. 힙큐로 만들기
3. 최솟값 제외 평균내기

둘 중에 하나는 없어야 함
K개 삭제를 없애려면
그냥 앞에서 K개를 평균구할 때 합에서 뺴고 개수도 K만큼 빼면 되긴 하는데
제외하는 최솟값이 K개에 없어야 가능한 거잖음

K개 삭제가 아니라 뒤에서부터 하나씩 힙큐에 넣으면 되는구나
이런 발상의 전환 같으니
"""
ans = 0

hq = [lst[N-1]]
cur_sum = lst[N-1]

for i in range(N-2, 0, -1):
    hg.heappush(hq, lst[i])
    cur_sum += lst[i]

    mean = (cur_sum - hq[0]) / (len(hq)-1)
    ans = max(ans, mean)

print(f'{ans:.2f}')
