class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_front(self, num):
        new_node = node(num)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def push_back(self, num):
        new_node = node(num)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def pop_front(self):
        # 이거 하고 비는 경우를 생각 해야하나?
        num = self.head.data

        if self.size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return num
    
    def pop_back(self):
        num = self.tail.data

        if self.size() == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return num
    
    def size(self):
        return self.length
    
    def empty(self):
        return int(self.length == 0)
    
    def front(self):
        return self.head.data
    
    def back(self):
        return self.tail.data
        


N = int(input())

my_dll = DLL()

for j in range(N):

    line = input().split()
    command = line[0]

    if command == 'push_front':
        num = int(line[1])
        my_dll.push_front(num)

    elif command == "push_back":
        num = int(line[1])
        my_dll.push_back(num)

    elif command == 'pop_front':
        print(my_dll.pop_front())

    elif command == 'pop_back':
        print(my_dll.pop_back())

    elif command == 'size':
        print(my_dll.size())

    elif command == 'empty':
        print(my_dll.empty())

    elif command == 'front':
        print(my_dll.front())

    else:
        print(my_dll.back())
