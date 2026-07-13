N, M, Q = map(int, input().split())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 이번 dll은 원형임
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

# circle = [DoubleLinkedList() for _ in range(M)]
circle = []

# node = {[None] + [Node(x) for x in range(1, N+1)]}
node = {}
for m in range(M):
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        continue
    circle.append(lst[1:])
    nums = lst[1:]
    for i in range(len(nums)):
        node[nums[i]] = Node(nums[i])

    for i in range(len(nums)):
        node[nums[i]].prev = node[nums[i-1]]
        node[nums[i-1]].next = node[nums[i]]
    
cmds = []
A = []
B = []
for q in range(Q):
    query = list(map(int, input().split()))
    cmds.append(query[0])
    A.append(query[1])
    
    if len(query) == 3:
        B.append(query[2])
    else:
        B.append(-1)

# a와 b를 잇고 (a의 next가 b)
# a의 next와 b의 prev를 잇고
def merge(a, b):
    aright = node[a].next
    bleft = node[b].prev

    node[a].next = node[b]
    node[b].prev = node[a]

    aright.prev = bleft
    bleft.next = aright

def divide(a, b):
    if a == b:  # 말이 안댐 문제에서 안줄 듯
        pass

    # print('divide', a, b)
    s, e = a, node[b].prev.data

    node[e].next.prev = node[s].prev
    node[s].prev.next = node[e].next

    node[e].next = node[s]
    node[s].prev = node[e]

for q in range(Q):
    cmd, a, b = cmds[q], A[q], B[q]

    if cmd == 1:
        merge(a, b)
    
    elif cmd == 2:
        divide(a, b)
    
    else:
        mn = a
        n = a
        while True:
            n = node[n].next.data
            if n == a:
                break
            if n < mn:
                mn = n
        n = mn
        while True:
            print(node[n].data, end=' ')

            n = node[n].prev.data
            if n == mn:
                break

