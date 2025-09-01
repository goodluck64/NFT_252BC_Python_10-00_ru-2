# queue
# stack

# enqueue (add to queue)
# dequeue (remove from queue)
# peek (get first element in queue)
# __len__
# clear
# contains

class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, value):
        self.__items.append(value)

    def dequeue(self):
        item = self.__items.pop(0)

        return item

q = Queue()

#