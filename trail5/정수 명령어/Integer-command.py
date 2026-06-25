T = int(input())

from sortedcontainers import SortedSet
for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    command = [op[0] for op in operations]
    x = [int(op[1]) for op in operations]

    ss = SortedSet()
    for i in range(k):
        cmd, n = command[i], x[i]

        if cmd == 'I':
            ss.add(n)
        elif cmd == 'D':
            if not ss:
                continue

            if n == 1:
                ss.remove(ss[-1])
            else:
                ss.remove(ss[0])

    if ss:
        print(ss[-1], ss[0])
    else:
        print('EMPTY')

"""
정수만 저장하는 큐가 있습니다. 이 큐에는 다음의 연산을 수행할 수 있습니다.

I n : 정수 n을 큐에 삽입합니다.
D 1 : 큐에서 최댓값을 삭제합니다.
D −1 : 큐에서 최솟값을 삭제합니다.
삽입되는 값은 중복되지 않으며, 
큐가 비어있을 때 D 연산이 주어지면 해당 연산은 무시합니다.
"""