n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

sf1 = set()
for n in arr1:
    sf1.add(n)

for m in arr2:
    if m in sf1:
        print(1)
    else:
        print(0)