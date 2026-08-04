from sortedcontainers import SortedSet

N, Q = map(int, input().split())

point = [list(map(int, input().split())) for _ in range(N)]
square = [list(map(int, input().split())) for _ in range(Q)]
arr = [[0]*(N+1) for _ in range(N+1)]
"""
어떤 점이 영역에 속한다는 건
x1 <= x <= x2
y1 <= y <= y2

그럼 인덱스로 바꾼다고 할 때
만약 좌표를 따로따로 하는거면
binary search를 해야 함. ~보다 큰 것들 중 가장 작은 값 찾기

그 전에, 일단 x 랑 y 압축하기
그래야 이 점 좌표를 어디 갖다 붙일지 binary search를 할 테니
"""

xss = SortedSet()
yss = SortedSet()

for i, j in point:
    xss.add(i)
    yss.add(j)

xdict = {}
ydict = {}

for i in range(len(xss)):
    xdict[xss[i]] = i+1

for i in range(len(yss)):
    ydict[yss[i]] = i+1

for i, j in point:
    arr[xdict[i]][ydict[j]] = 1

preSum = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        preSum[i][j] = arr[i][j] + preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1]

def myp(arr):
    for row in arr:
        for val in row:
            print(f'{val:>2}', end=' ')
        print()
    print()

xlst = list(xss)
ylst = list(yss)


def bisect_left(tlst, p):
    left, right = 0, len(tlst)

    while (left < right):
        mid = (left + right) // 2
        if tlst[mid] < p:
            left = mid + 1
        else:
            right = mid
        
    return left

def bisect_right(tlst, p):
    left, right = 0, len(tlst)

    while (left < right):
        mid = (left + right) // 2
        if tlst[mid] <= p:
            left = mid + 1
        else:
            right = mid
    
    return left



"""
이제 사각형의 네 점에 대해 이 점이 과연
어느 점의 왼쪽(위쪽)에 있는지, 어느 점의 오른쪽(아래쪽)에 있는지 찾기
ex)
    x1이 xss의 점들 중 어떤 점 바로 왼쪽인지 찾기   (인덱스)
    x2가 xss의 점들 중 어떤 점 바로 오른쪽인지 찾기 (인덱스)
    y에서도 반복

그러고 포인트를 돌면서 x 사이, y 사이 있는 애들을 찾아주면 되는데
Q가 30만인데 이걸 매번 반복하면 시간초과가 나겠지? 안해봐도 알겠지?

그러니까 미리 prefix sum을 구해놓아야 한다~
이거는 압축된 평면에서 하는 게 맞을거고
일단 preSum 만듭시다

아닌가? 애초에 점 위치 기준 압축이라 preSum이 무조건 1씩 늘어나는 거 같은데
아니네 점 위치 기준이라고 해도 그 2D 평면이 꽉 차진 않는구나

세팅 다 끝남. 진짜 binary search만 하면 됨
그래도 배운 적 있으니 구현을 해보자
"""
# myp(arr)
# myp(preSum)

# print(xlst)
# print(ylst)

for x1, y1, x2, y2 in square:

    si = bisect_left(xlst, x1)
    sj = bisect_left(ylst, y1)

    ei = bisect_right(xlst, x2)
    ej = bisect_right(ylst, y2)

    cnt = preSum[ei][ej] - preSum[si][ej] - preSum[ei][sj] + preSum[si][sj]
    # print(x1, y1, x2, y2)
    # print(si, sj, ei, ej)
    print(cnt)