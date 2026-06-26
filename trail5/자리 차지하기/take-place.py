N, M = map(int, input().split())
lst = list(map(int, input().split()))

"""
앉고싶은 자리 범위가 주어지고
그거에 맞게 최대한 많이 사람 앉히기
못앉는 사람 나오면 종료

그럼 누군가를 일단 최대 자리에 앉히고,
만약 거기 누가 있으면 하나 줄여보고 반복
이러면 O(N^2)아닌가

bisect 활용해야 하는가봄

일단 사람은 가능한 뒤에 앉히는 게 미래를 위해 좋음
그러면 n 이하 값 중 최대값에 앉히면 되는거고

첫번째 사람 입력으로 받는다고 할 때 그 사람 최대 자리를 n이라고 하자
SortedSet에 있는 값중에 n보다 작은 최초의 값을 찾아야 하는 거니까
다 음수로 처리하면 음수에서 -n보다 크거나 같은 최초의 값 찾을 수 있고
거기 앉히고 cnt += 1 한 뒤에 그 값 삭제하면 됨

괜히 기대했죠? 객관적으로 봐도 아니죠?
자기 객관화를 해봅시ekkkk
"""
from sortedcontainers import SortedSet
ss = SortedSet([x for x in range(1, M+2)])

cnt = 0
# print(ss)
for i, n in enumerate(lst):
    idx = ss.bisect_right(n)
    if idx == len(ss) or idx == 0:
        break

    num = ss[idx-1]
    # print(ss)
    # print('smaller than', n, 'is', num, 'at', idx-1)
    ss.remove(num)
    cnt += 1

print(cnt)