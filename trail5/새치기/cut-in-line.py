N, M, Q = map(int, input().split())
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.nset = set()
    
    def insert_front(self, a, b, pos):
        if pos == 0:
            if self.head:
                self.head.prev = node[b]
                node[b].next = self.head
            self.head = node[a]

            if not self.tail:
                self.tail = node[b]
        else:
            if node[pos].prev:
                node[pos].prev.next = node[a]
            node[a].prev = node[pos].prev
            
            node[pos].prev = node[b]
            node[b].next = node[pos]
            if pos == self.head.data:
                self.head = node[a]
        
        val = a
        while True:
            self.nset.add(val)
            self.length += 1

            if val == b:
                break
            val = node[val].next.data

    def insert_back(self, a):
        if not self.head:
            self.head = node[a]
        
        if self.tail:
            self.tail.next = node[a]
            node[a].prev = self.tail

        self.tail = node[a]

        self.length += 1
        self.nset.add(a)
        

    def pop_range(self, a, b):
        # 아아아아아아악
        if a == self.head.data and node[b].next:
            self.head = node[b].next
        if b == self.tail.data and node[a].prev:
            self.tail = node[a].prev

        if node[a].prev:
            node[a].prev.next = node[b].next
        if node[b].next:
            node[b].next.prev = node[a].prev

        val = a
        while True:
            self.nset.remove(val)
            self.length -= 1

            if val == b:
                break
            val = node[val].next.data

        if self.length == 0:
            self.head = None
            self.tail = None
            
line = [[0] * N for _ in range(M)]
line_size = [0] * M
cmd = [[0] * 4 for _ in range(Q)]

node = [0] + [Node(x) for x in range(1, N+1)]
dll = [DoubleLinkedList() for _ in range(M)]

for i in range(M):
    nums = list(map(int, input().split()))
    if nums[0] == -1:
        line_size[i] = 0
        continue
    line_size[i] = nums[0]
    for j in range(nums[0]):
        line[i][j] = nums[j + 1]

for i in range(M):
    for j in range(N):
        val = line[i][j]
        if val == 0:
            break
        dll[i].insert_back(val)

for i in range(Q):
    query = list(map(int, input().split()))
    cmd[i][0] = query[0]
    if query[0] == 1:
        cmd[i][1] = query[1]
        cmd[i][2] = query[2]
    elif query[0] == 2:
        cmd[i][1] = query[1]
    elif query[0] == 3:
        cmd[i][1] = query[1]
        cmd[i][2] = query[2]
        cmd[i][3] = query[3]

# for i in range(M):
#     nn = dll[i].head
#     print(dll[i].nset, dll[i].length)
#     while True:
#         print(nn.data, end=' ')
#         if not nn.next:
#             break
#         nn = nn.next
#     print()
# print()

for q in range(Q):
    cm, a, b, c = cmd[q]
    for i in range(M):
        if a in dll[i].nset:
            ai = i
        if b in dll[i].nset:
            bi = i
        if c in dll[i].nset:
            ci = i
    
    if cm == 1:
        dll[ai].pop_range(a, a)
        dll[bi].insert_front(a, a, b)
    
    if cm == 2:
        dll[ai].pop_range(a, a)
        node[a].prev = None
        node[a].next = None
    
    if cm == 3:
        dll[ai].pop_range(a, b)
        dll[ci].insert_front(a, b, c)

for i in range(M):
    nn = dll[i].head
    if not nn:
        print(-1)
        continue
    # print(dll[i].nset, dll[i].length)
    while True:
        print(nn.data, end=' ')
        if not nn.next:
            break
        nn = nn.next
    print()