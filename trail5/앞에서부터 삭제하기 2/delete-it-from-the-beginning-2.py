N = int(input())
lst = list(map(int, input().split()))

import heapq as hf
"""
중복이 있어서 힙큐로 풀어야 하네....
힙큐를 매번 만들기는 좀 그렇고
매번 이진탐색 하면서 삭제할 값 어딨나 찾기도 좀 그렇고

역순으로 미리 다 빼놓고 하나씩 더하는 걸로

"""
# N-2개까지 제외된 상태
hq = []
hf.heappush(hq, lst[-1])

cur_sum, ans = lst[-1], 0

for k in range(N-2, 0, -1):
    # k번째 값 힙큐에 추가 (삭제한 후 상황)
    hf.heappush(hq, lst[k])
    cur_sum += lst[k]

    # 가장 작은 값 제외한 평균 구하기
    mean = (cur_sum - hq[0]) / (len(hq)-1)

    if mean > ans:
        ans = mean

print(f'{ans:.2f}')