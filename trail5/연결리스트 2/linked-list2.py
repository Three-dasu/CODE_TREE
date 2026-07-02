N = int(input())
Q = int(input())

type_arr = []
i_arr = []
j_arr = []

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

for _ in range(Q):
    query = list(map(int, input().split()))
    type_arr.append(query[0])
    i_arr.append(query[1])
    if query[0] in [2, 3]:
        j_arr.append(query[2])
    else:
        j_arr.append(0)

nlst = [0]
for n in range(1, N+1):
    nlst.append(Node(n))

for q in range(Q):
    cmd, i, j = type_arr[q], i_arr[q], j_arr[q]

    if cmd == 1:
        if nlst[i].prev:
            nlst[i].prev.next = nlst[i].next
        if nlst[i].next:
            nlst[i].next.prev = nlst[i].prev
        nlst[i].prev = None
        nlst[i].next = None

    elif cmd == 2:
        # i번 
        # print(nlst[j])
        nlst[j].prev = nlst[i].prev
        nlst[j].next = nlst[i]
        if nlst[i].prev:
            nlst[i].prev.next = nlst[j]
        nlst[i].prev = nlst[j]
        

    elif cmd == 3:
        nlst[j].prev = nlst[i]
        nlst[j].next = nlst[i].next
        if nlst[i].next:
            nlst[i].next.prev = nlst[j]
        nlst[i].next = nlst[j]


    else:
        # print(0)
        pre = nlst[i].prev.data if nlst[i].prev else 0
        nex = nlst[i].next.data if nlst[i].next else 0
        print(pre, nex)

for n in range(1, N+1):
    print(nlst[n].next.data if nlst[n].next else 0, end=' ')

