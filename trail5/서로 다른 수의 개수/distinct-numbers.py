N = int(input())
lst = list(map(int, input().split()))

sf = set()
for n in lst:
    sf.add(n)

print(len(sf))