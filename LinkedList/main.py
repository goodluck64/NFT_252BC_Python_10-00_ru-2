class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedListIterator:
    def __init__(self, start):
        self.__start = start
        self.__current = None

    def __next__(self):
        if self.__current is None:
            self.__current = self.__start
        else:
            self.__current = self.__current.next

        if self.__current is None:
            raise StopIteration

        return self.__current.value

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def add_last(self, value):
        new_node = Node(value)

        if self.__tail is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

        self.__length += 1

        return new_node

    def __iter__(self):
        return LinkedListIterator(self.__head)

    def __len__(self):
        return self.__length


llist = LinkedList()

llist.add_last(10)
llist.add_last(20)
llist.add_last(30)
llist.add_last(40)

for item in llist:
    print(item)


