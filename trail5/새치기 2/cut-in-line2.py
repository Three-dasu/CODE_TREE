N, M, Q = map(int, input().split())
names = input().split()

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

node = [None] + [Node(x) for x in names]
node_dic = {-1: -1}
v = [0]*(N+1)
seq = [Node(-1) for _ in range(M)]

for i in range(N):
    node_dic[names[i]] = i+1
"""
X = N // M
i번째 사람은 i//X번 줄의 (i-1)%(X+1) 번째로 서 있음
근데 그냥 첫 줄부터 X명씩 세운다는 거 아닌가?
"""
# 줄마다 순회하며 사람들 이어주기
X = N // M
# print(X)
for i in range(1, N+1):
    m = (i-1)//X        # 올림이지만 줄은 0idx로 할거임
    j = (i-1) % (X) + 1 # 그치만 인덱스는 1idx
    # print(m, 'th line', j, 'th person')
    
    if j == 0:
        continue

    # 매 line의 첫번째 노드는 더미랑 연결
    if j == 1:
        seq[m].next = node[i]
        node[i].prev = seq[m]
    else:
        node[i-1].next = node[i]
        node[i].prev = node[i-1]


def cut_in_line(a, b, c):
    left = node[a].prev
    right = node[b].next
    befo = node[c].prev

    if left:
        left.next = right
    if right:
        right.prev = left
    node[a].prev = befo
    if befo:
        befo.next = node[a]
    node[b].next = node[c]
    node[c].prev = node[b]

def go_home(a):
    left = node[a].prev
    right = node[a].next

    if left:
        left.next = right
    if right:
        right.prev = left
    
    node[a].prev = None
    node[a].next = None
    v[a] = 1





command = []

for _ in range(Q):
    line = input().split()
    cmd = int(line[0])
    command.append(cmd)

    if cmd == 1:
        a, b = line[1], line[2]
        a, b = node_dic[a], node_dic[b]
        cut_in_line(a, a, b)

    elif cmd == 2:
        a = line[1]
        a = node_dic[a]
        go_home(a)

    else:
        a, b, c = line[1], line[2], line[3]
        a, b, c = node_dic[a], node_dic[b], node_dic[c]
        cut_in_line(a, b, c)

# 출력
for m in range(M):
    nn = seq[m].next

    while True:
        print(nn.data, end=' ')

        if not nn.next:
            break
        nn = nn.next
    print()