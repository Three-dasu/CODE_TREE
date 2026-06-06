N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort(lambda x: (x[1]))
cnt, pos = 0, -1
for i, (a, b) in enumerate(lst):
    if pos >= a:
        continue
    
    pos = b
    cnt += 1

print(cnt)
