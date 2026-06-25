N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0], 0))

import heapq
hq = []

for i in range(N):
    cmd, n = commands[i]

    if cmd == 'push':
        heapq.heappush(hq, -n)
    elif cmd == 'pop':
        print(-heapq.heappop(hq))
    elif cmd == 'size':
        print(len(hq))
    elif cmd == 'empty':
        print(1 if len(hq)==0 else 0)
    else:
        print(-hq[0])