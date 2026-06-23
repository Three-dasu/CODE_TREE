n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

qwe = {}

for x, y in points:
    if x not in qwe:
        qwe[x] = [y]
    else:
        qwe[x].append(y)

ans = 0
for x, lst in qwe.items():
    ans += min(lst)

print(ans)