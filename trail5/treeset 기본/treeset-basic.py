n = int(input())
command = []
x = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        x.append(int(line[1]))
    else:
        x.append(0)
"""
add x : 숫자 x를 treeset에 추가합니다. 중복되는 경우 무시합니다.
remove x : 숫자 x를 treeset에서 제거합니다. 잘못된 입력은 주어지지 않습니다.
find x : 숫자 x가 treeset에 있는지를 판단합니다. 있다면 true, 없다면 false를 출력합니다.
lower_bound x : treeset에서 x보다 같거나 큰 최초의 숫자를 출력합니다. 만약 없다면 None을 출력합니다.
upper_bound x : treeset에서 x보다 큰 최초의 숫자를 출력합니다. 만약 없다면 None을 출력합니다.
largest : treeset에서 가장 큰 숫자를 출력합니다. 만약 treeset이 비어있다면 None을 출력합니다.
smallest : treeset에서 가장 작은 숫자를 출력합니다. 만약 treeset이 비어있다면 None을 출력합니다.
"""
from sortedcontainers import SortedSet
ss = SortedSet()

for i in range(n):
    cmd, num = command[i], x[i]
    if cmd == 'add':
        ss.add(num)
    elif cmd =='remove':
        ss.remove(num)
    elif cmd == 'find':
        print('true' if num in ss else 'false')
    elif cmd == 'lower_bound':
        idx = ss.bisect_left(num)
        if idx == len(ss):
            print('None')
            continue
        print(ss[idx])
    elif cmd == 'upper_bound':
        idx = ss.bisect_right(num)
        if idx == len(ss):
            print('None')
            continue
        print(ss[idx])
    elif cmd == 'largest':
        if not ss:
            print('None')
            continue
        print(ss[-1])
    else:
        if not ss:
            print('None')
            continue
        print(ss[0])



