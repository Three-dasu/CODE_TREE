n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

from sortedcontainers import SortedDict

qwe = SortedDict()

for i in range(n):
    if cmd[i] == 'add':
        qwe[k[i]] = v[i]
    elif cmd[i] == 'remove':
        del qwe[k[i]]
    elif cmd[i] == 'find':
        if k[i] in qwe:
            print(qwe[k[i]])
        else:
            print('None')
    else:
        if qwe:
            for kk in qwe:
                print(qwe[kk], end=' ')
            print()
        else:
            print('None')