N, M = map(int, input().split())
lst = list(map(int, input().split()))

"""
0부터 N까지 수들이 정확히 하나씩 놓여 있습니다.
이때 M개의 수를 순서대로 하나씩 제거해보며,
제거한 이후 남은 수들로 만들 수 있는 수열 중
연속하여 나타나는 수들로만 이루어진 수열의 최장 길이를
구하는 프로그램을 작성해보세요.

예를 들어 처음에 [0, 1, 2, 3, 4, 5, 6, 7, 8]이 있었는데
3을 제거하게 된다면, [0, 1, 2, 4, 5, 6, 7, 8]이 남게 되므로
연속한 숫자들로 만들 수 있는 수열 중 최장 수열은
[4, 5, 6, 7, 8]이 되므로 최장 길이는 5가 됩니다.


"""

from sortedcontainers import SortedSet, SortedList
import heapq as hf
ss = SortedSet([-1, N+1])
lns = SortedList([N+1])

for x in lst:
    idx = ss.bisect_right(x)
    left, right = ss[idx-1], ss[idx]

    len_to_divide = right-left-1

    lns.remove(len_to_divide)
    lns.add(x - left - 1)
    lns.add(right - x - 1)

    ss.add(x)

    print(lns[-1])
    # 0, 1, 2, 3, 4, 5, 6, 7, 8
    # 0, 1 ,2 ,3     5, 6, 7, 8
    # 0, 1, 2, 3,    5, 6,    8

