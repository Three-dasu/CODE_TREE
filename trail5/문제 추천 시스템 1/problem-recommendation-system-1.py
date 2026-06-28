n = int(input())

from sortedcontainers import SortedSet
ss = SortedSet()

for _ in range(n):
    p, l = map(int, input().split())
    ss.add((l, p))

m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        commands.append((cmd[0], int(cmd[1])))
    else:
        commands.append((cmd[0], int(cmd[1]), int(cmd[2])))



for i in range(m):
    if commands[i][0] == "rc":
        x = commands[i][1]
        if x == 1:
            print(ss[-1][1])
        else:
            print(ss[0][1])
    
    elif commands[i][0] == "ad":
        p, l = commands[i][1], commands[i][2]
        ss.add((l, p))
    
    else:
        p, l = commands[i][1], commands[i][2]
        ss.remove((l, p))