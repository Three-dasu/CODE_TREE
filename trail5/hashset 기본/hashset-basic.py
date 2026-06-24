n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

sf = set()
for cmd, val in zip(commands, x):
    if cmd == 'add':
        sf.add(val)
    elif cmd == 'remove':
        sf.remove(val)
    elif cmd == 'find':
        print('true' if val in sf else 'false')
