n = int(input())
words = [input() for _ in range(n)]

from sortedcontainers import SortedDict as SD

sdf = SD()

for word in words:
    if word in sdf:
        sdf[word] += 1
    else:
        sdf[word] = 1

for k, v in sdf.items():
    print(k, v)