################Task01##############
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__count = 0

    def get_counter(self):
        return self.__count

    def pop(self):
        val = super().pop()
        self.__count += 1
        return val


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
################Task02##############
class QueueError(Exception):
    pass
class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.insert(0, elem)


    def get(self):
        if not len(self.list_queue):
            raise QueueError
        else:
            elem = self.list_queue.pop()
        return elem
que = Queue()
que.put(1)
que.put("dog")
que.put(False)
# print(que.get())
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
################Task03##############
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, element):
        self.__queue.insert(0, element)

    def get(self):
        if not self.__queue:
            raise QueueError("Queue is empty")
        return self.__queue.pop()

    def isempty(self):
        return not bool(self.__queue)
class SuperQueue(Queue):
    pass

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
