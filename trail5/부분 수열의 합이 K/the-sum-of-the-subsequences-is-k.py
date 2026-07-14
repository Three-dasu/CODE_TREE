N, K = map(int, input().split())
lst = list(map(int, input().split()))

prefix = [0]*(N+1)

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + lst[i-1]

cnt = 0
for i in range(N+1):
    for j in range(i+1, N+1):
        if prefix[j]-prefix[i] == K:
            cnt += 1

print(cnt)
