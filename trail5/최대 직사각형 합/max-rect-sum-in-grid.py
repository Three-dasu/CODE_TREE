N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

preSum = [[0]*(N+1) for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(1, N+1):
        preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + arr[i-1][j-1]

def myp(arr):
    for row in arr:
        for val in row:
            print(f"{val: >3}", end=' ')
        print()
    print()


# myp(preSum)

ans = -float("inf")
colmin = float("inf")


for i in range(1, N+1):     # 행1
    for j in range(1, i+1): # 행2
        colmin = 0
        mincol = 0

        for k in range(1, N+1): #열
            
            colSum = preSum[i][k] - preSum[j-1][k]

            val = colSum - colmin
            ans = max(ans, val)

            if colSum < colmin:
                colmin = colSum
                mincol = k


print(ans)