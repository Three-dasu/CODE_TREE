Q = int(input())

option = []
aa = []
bb = []

for _ in range(Q):
    query = list(map(int, input().split()))
    option.append(query[0])
    if query[0] == 1 or query[0] == 2:
        aa.append(query[1])
        bb.append(query[2])
    else:
        aa.append(query[1])
        bb.append(0)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
cur = 1
nlst = [0] + [Node(cur)]

for q in range(Q):
    cmd, a, b = option[q], aa[q], bb[q]

    # a번 학생 뒤에 현재 다음 번호부터 b명 세우기
    if cmd == 1:
        for i in range(cur+1, cur+1+b):
            nlst.append(Node(i))
            if i == cur+1:
                continue

            nlst[i].prev = nlst[i-1]
            nlst[i-1].next = nlst[i]

        if nlst[a].next:
            nlst[cur+b].next = nlst[a].next
            nlst[a].next.prev = nlst[cur+b]

        nlst[cur+1].prev = nlst[a]
        nlst[a].next = nlst[cur+1]
        cur += b


    # a번 학생 앞에 현재 다음 번호부터 b명 세우기
    elif cmd == 2:
        for i in range(cur+1, cur+1+b):
            nlst.append(Node(i))
            if i == cur+1:
                continue
            
            nlst[i].prev = nlst[i-1]
            nlst[i-1].next = nlst[i]

        if nlst[a].prev:
            nlst[cur+1].prev = nlst[a].prev
            nlst[a].prev.next = nlst[cur+1]

        nlst[a].prev = nlst[cur+b]
        nlst[cur+b].next = nlst[a]
        cur += b

    # a번 앞뒤 번호 출력, 한명이라도 없으면 -1 출력
    else:
        front = -1 if not nlst[a].prev else nlst[a].prev.data
        back = -1 if not nlst[a].next else nlst[a].next.data
        if front == -1 or back == -1:
            print(-1)
        else:
            print(front, back)