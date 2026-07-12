N, M = map(int, input().split())
knight = list(map(int, input().split()))
call = [int(input()) for _ in range(M)]

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
nlst = [Node(x) for x in knight]
elr = {x:i for i, x in enumerate(knight)}


for i in range(N-1):
    nlst[i].next = nlst[i+1]
    nlst[i+1].prev = nlst[i]

nlst[N-1].next = nlst[0]
nlst[0].prev = nlst[N-1]

for m in call:

    cur = nlst[elr[m]]
    # 연결 잇기
    cur.prev.next = cur.next
    cur.next.prev = cur.prev

    # 양옆 (next부터) 부르기
    print(cur.next.data, cur.prev.data)

    # 연결 끊기
    cur.next = None
    cur.prev = None

    del elr[m]

