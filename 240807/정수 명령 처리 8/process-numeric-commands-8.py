# 노드를 만들어주는 클래스
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data) :
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None :
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        else :
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num += 1

    def push_back(self, new_data) :
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None :
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

        else :
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        self.node_num += 1

    def pop_front(self) :
        if self.head == None :
            print('List is empty')

        elif self.head.next == None :
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data

        else :
            temp = self.head

            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.node_num -= 1
            return temp.data

    def pop_back(self) :
        if self.tail == None :
            print('List is empty')

        elif self.tail.prev == None :
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data

        else :
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            return temp.data

    def size(self) :
        return self.node_num

    def empty(self) :
        return self.node_num == 0

    def front(self) :
        if self.head == None :
            print('List is empty') 

        else :
            return self.head.data

    def back(self) :
        if self.tail == None :
            print('List is empty')

        else :
            return self.tail.data

n = int(input())


D = DoublyLinkedList()
for _ in range(n) :
    order = input()
    
    if order.startswith('push_front') :
        _, num = tuple(order.split())

        D.push_front(num)
    
    elif order.startswith('push_back') :
        _, num = tuple(order.split())

        D.push_back(num)

    elif order.startswith('pop_front') :
        print(D.pop_front())

    elif order.startswith('pop_back') :
        print(D.pop_back())

    elif order.startswith('size') :
        print(D.size())

    elif order.startswith('empty') :
        ret = D.empty()
        if ret == 1:
            print(1)
        else :
            print(0)

    elif order.startswith('front') :
        print(D.front())
    
    else :
        print(D.back())