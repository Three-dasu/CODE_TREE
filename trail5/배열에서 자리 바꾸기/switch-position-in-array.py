class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


N = int(input())
Q = int(input())

# 0과 N+1은 센티널 노드
nodes = [Node(i) for i in range(N + 2)]

for i in range(N + 1):
    nodes[i].next = nodes[i + 1]
    nodes[i + 1].prev = nodes[i]


def swap_segments(a, b, c, d):
    """
    연결 리스트에서 [a ... b] 구간과 [c ... d] 구간을 교환한다.

    두 구간은 겹치지 않고,
    각각 a에서 b, c에서 d 방향으로 연결되어 있다.
    """
    A = nodes[a]
    B = nodes[b]
    C = nodes[c]
    D = nodes[d]

    a_prev = A.prev
    b_next = B.next
    c_prev = C.prev
    d_next = D.next

    # [a ... b][c ... d]처럼 두 구간이 붙어 있는 경우
    if B.next is C:
        a_prev.next = C
        C.prev = a_prev

        D.next = A
        A.prev = D

        B.next = d_next
        d_next.prev = B

    # [c ... d][a ... b]처럼 반대 방향으로 붙어 있는 경우
    elif D.next is A:
        c_prev.next = A
        A.prev = c_prev

        B.next = C
        C.prev = B

        D.next = b_next
        b_next.prev = D

    # 두 구간 사이에 다른 노드들이 있는 경우
    else:
        # a...b가 있던 자리에 c...d 연결
        a_prev.next = C
        C.prev = a_prev

        D.next = b_next
        b_next.prev = D

        # c...d가 있던 자리에 a...b 연결
        c_prev.next = A
        A.prev = c_prev

        B.next = d_next
        d_next.prev = B


for _ in range(Q):
    a, b, c, d = map(int, input().split())
    swap_segments(a, b, c, d)


cur = nodes[0].next

while cur is not nodes[N + 1]:
    print(cur.data, end=" ")
    cur = cur.next