N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

def bfs(left, right):
    
    if not left <= arr[0][0] <= right:
        return False

    q = deque()
    v = [[0]*N for _ in range(N)]

    q.append((0, 0))
    v[0][0] = 1

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (N-1, N-1):
            return True

        for di, dj in ((1, 0), (0, 1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and left <= arr[ni][nj] <= right:
                q.append((ni, nj))
                v[ni][nj] = 1
    
    return False

nums = set()
for i in range(N):
    for j in range(N):
        nums.add(arr[i][j])
nums = sorted(list(nums))

l, r = 0, 0
mn = 2**31

while l < len(nums) and r < len(nums):
    left = nums[l]
    right = nums[r]

    if bfs(left, right):
        mn = min(mn, right-left)
        l += 1
    else:
        r += 1

print(mn)