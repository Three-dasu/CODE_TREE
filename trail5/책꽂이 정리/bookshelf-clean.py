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

    def pop_node_front(self):
        if self.length == 1:
            val = self.head.data
            self.head = None
            self.tail = None
            self.length -= 1
            return val

        elif self.head:
            val = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return val
        else:
            print('No head in this DLL')

    def pop_node_back(self):
        if self.length == 1:
            val = self.tail.data
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        elif self.tail:
            val = self.tail.data
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return val
        else:
            print('No tail in this DLL')

    def insert_node_front(self, node):
        self.length += 1
        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node
        self.head.prev = None
        if not self.tail:
            self.tail = node
            self.tail.next = None

    def insert_node_back(self, node):
        self.length += 1
        if not self.head:
            self.head = node
            self.head.prev = None
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.tail.next = None

    # DLL 비우기
    def empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def lenlen(self):
        return self.length
        
N, K = map(int, input().split())
Q = int(input())
type_arr = []
i_arr = []
j_arr = []
for _ in range(Q):
    t, x, y = map(int, input().split())
    type_arr.append(t)
    i_arr.append(x)
    j_arr.append(y)

node = [0] + [Node(n) for n in range(1, N+1)]
dll =[0] + [DoubleLinkedList() for _ in range(K)]
for n in range(1, N+1):
    dll[1].insert_node_back(node[n])

for q in range(Q):
    cmd, i, j = type_arr[q], i_arr[q], j_arr[q]
    if dll[i].length == 0:
        continue
    if cmd == 1:
        val = dll[i].pop_node_front()
        # node[val].next = None
        dll[j].insert_node_back(node[val])

    if cmd == 2:
        val = dll[i].pop_node_back()
        # node[val].prev = None
        dll[j].insert_node_front(node[val])
    
    if cmd == 3:
        if i == j:
            continue

        h, t = dll[i].head.data, dll[i].tail.data

        if not dll[j].head:
            dll[j].head = node[h]
            dll[j].tail = node[t]
        else:
            dll[j].head.prev = node[t]
            node[t].next = dll[j].head
            dll[j].head = node[h]
        dll[j].length += dll[i].length

        dll[i].empty()

    if cmd == 4:
        if i == j:
            continue

        h, t = dll[i].head.data, dll[i].tail.data

        if not dll[j].head:
            dll[j].head = node[h]
            dll[j].tail = node[t]
        else:
            dll[j].tail.next = node[h]
            node[h].prev = dll[j].tail
            dll[j].tail = node[t]
        
        dll[j].length += dll[i].length
        
        dll[i].empty()

for k in range(1, K+1):
    cnode = dll[k].head
    if not cnode:
        print(0)
        continue
    print(dll[k].lenlen(), end=' ')

    if cnode:
        while True:
            print(cnode.data, end=' ')
            cnode = cnode.next
            if not cnode:
                break
    print()


    