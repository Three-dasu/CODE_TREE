N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]

def cal_dist(x1, y1, x2, y2):
    # print(x1, y1, x2, y2)
    # print(abs(x1-x2), abs(y1-y2))
    return abs(x1-x2) + abs(y1-y2)

llst = [0] * N
rlst = [0] * N

for i in range(N-1):
    dist = cal_dist(point[i][0], point[i][1], point[i+1][0], point[i+1][1])
    llst[i+1] = dist + llst[i]

for i in range(N-1, 0, -1):

    dist = cal_dist(point[i][0], point[i][1], point[i-1][0], point[i-1][1])
    rlst[i-1] = dist + rlst[i]
#     print(rlst)

# print(llst)
# print(rlst)

ans = float("inf")
for i in range(1, N-1):
    tmp = cal_dist(point[i-1][0], point[i-1][1], point[i+1][0], point[i+1][1])\
            + llst[i-1] + rlst[i+1]
    if tmp < ans:
        ans = tmp

print(ans)
