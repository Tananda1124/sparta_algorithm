class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:  # 첫 노드가 비어있으면 첫 노드에 append한다.
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next  # cur이 None이 아니라면, None이 나올 때까지 옆 노드로 이동한다.
        cur.next = Node(data)  # 새로운 node 생성하기

    def print_all(self):
        print("Now printing all..")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
