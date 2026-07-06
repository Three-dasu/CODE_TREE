N, Q = map(int, input().split())
cities = list(input().split())

option = []
new_city = [None] * Q

for i in range(Q):
    query = input().split()
    option.append(int(query[0]))
    if option[i] == 4:
        new_city[i] = query[1]

class Node:
    def __init__(self, idx, data):
        self.idx = idx
        self.data = data
        self.prev = None
        self.next = None

node = [Node(idx, x) for idx, x in enumerate(cities)]
for n in range(1, N):
    node[n].prev = node[n-1]
    node[n-1].next = node[n]
node[0].prev = node[N-1]
node[N-1].next = node[0]


p = 0
idx = N
for q in range(Q):
    if option[q] == 1 and node[p].next:
        p = node[p].next.idx

    elif option[q] == 2 and node[p].prev:
        p = node[p].prev.idx
        
    elif option[q] == 3 and node[p].next:

        if node[p].next.next != node[p]:
            node[p].next.next.prev = node[p]

            node[p].next = node[p].next.next

    
    else:
        new_node = Node(idx, new_city[q])
        idx += 1
        node.append(new_node)
        new_node.prev = node[p]
        new_node.next = node[p].next
        if node[p].next:
            node[p].next.prev = new_node
        node[p].next = new_node
    
    
    left = node[p].prev.data if node[p].prev else -1
    right = node[p].next.data if node[p].next else -1

    if left == -1 or right == -1 or left == right:
        print(-1)
    else:
        print(left, right)