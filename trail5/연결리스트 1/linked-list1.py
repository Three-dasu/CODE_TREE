S_init = input()
N = int(input())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def insert_front(self, cur):
        self.next = cur
        if cur.prev:
            self.prev = cur.prev
            cur.prev.next = self
        cur.prev = self
    
    def insert_back(self, cur):
        self.prev = cur
        
        if cur.next:
            self.next = cur.next
            cur.next.prev = self
        cur.next = self

command = []
S_value = []

for _ in range(N):
    line = input().split()
    cmd = int(line[0])
    command.append(cmd)
    if cmd == 1 or cmd == 2:
        S_value.append(line[1])
    else:
        S_value.append("")

def myp():
        pre = init_node.prev.data if init_node.prev else '(Null)'
        cur = init_node.data
        nex = init_node.next.data if init_node.next else '(Null)'
        print(pre, cur, nex)

init_node = Node(S_init)

for i in range(N):
    cmd, sval = command[i], S_value[i]

    if cmd == 1:
        new_node = Node(sval)
        new_node.insert_front(init_node)
        myp()
    
    elif cmd == 2:
        new_node = Node(sval)
        new_node.insert_back(init_node)
        myp()
    
    elif cmd == 3:
        if init_node.prev:
            left_node = init_node.prev
            left_left_node = init_node.prev.prev
            left_val = left_node.data
            init_val = init_node.data
            right_node = init_node.next
            
            init_node.prev = left_left_node
            init_node.next = left_node
            init_node.data = left_val

            if right_node:
                right_node.prev = left_node
            
            left_node.prev = init_node
            left_node.next = right_node
            left_node.data = init_val
            myp()
        else:
            myp()
    
    else:
        if init_node.next:
            left_node = init_node.prev
            right_node = init_node.next
            right_val = right_node.data
            init_val = init_node.data
            right_right_node = init_node.next.next
            
            init_node.prev = right_node
            init_node.next = right_right_node
            init_node.data = right_val

            if left_node:
                left_node.next = right_node
            
            right_node.prev = left_node
            right_node.next = init_node
            right_node.data = init_val

            myp()
        else:
            myp()


