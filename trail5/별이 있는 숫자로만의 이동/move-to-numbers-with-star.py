N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def myp(arr):
    for row in arr:
        for val in row:
            print(f"{val:>2}", end=' ')
        print()
    print()
    
narr = [[0]*(2*N) for _ in range(2*N)]

for i in range(N):
    for j in range(N):
        narr[i+j][i-j+N] = arr[i][j]

preSum = [[0]*(2*N+1) for _ in range(2*N+1)]

for i in range(1, 2*N+1):
    for j in range(1, 2*N+1):
        preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + narr[i-1][j-1]

# myp(preSum)

ans = 0
for u in range(N):
    for v in range(N):
        i, j = u + v, u - v + N
        si, sj = i-K, j-K
        ei, ej = i+K, j+K

        if si < 1:      si = 1
        if sj < 1:      sj = 1
        if ei > 2*N:    ei = 2*N
        if ej > 2*N:    ej = 2*N

        tmp = preSum[ei][ej] - preSum[si-1][ej] - preSum[ei][sj-1] + preSum[si-1][sj-1]

        ans = max(tmp, ans)


print(ans)



