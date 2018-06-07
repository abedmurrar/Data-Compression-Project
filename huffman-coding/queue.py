MAX_SIZE = 256

class PriorityQueueNode:
    def __init__(self, val=None, priority=None, next=None):
        self.val = val
        self.priority = priority
        self.next = next

    def setVal(self, val):
        self.val = val

    def getVal(self):
        return self.val

    def setPriority(self, priority):
        self.priority = priority

    def getPriority(self):
        return self.priority

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

class PriorityQueue:
    def __init__(self, size=0, first=None):
        self.size = size
        self.first = first

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getFirst(self):
        return self.first

    def setFirst(self, first):
        self.first = first

def addPQueue(queue, val, priority):
    if queue.getSize() is MAX_SIZE:
        print('Queue is full')
        return
    else:
        aux = PriorityQueueNode()
        aux.setPriority(priority)
        aux.setVal(val)

        if queue.getSize() is 0 or queue.getFirst() is None:
            aux.setNext(None)
            queue.setFirst(aux)
            queue.setSize(1)
            return
        else:
            if priority <= queue.getFirst().getPriority():
                aux.setNext(queue.getFirst())
                queue.setFirst(aux)
                queue.setSize(queue.getSize() + 1)
                return
            else:
                iterator = queue.getFirst()
                while (iterator.getNext() is not None):
                    if priority <= iterator.getNext().getPriority():
                        aux.setNext(iterator.getNext())
                        iterator.setNext(aux)
                        queue.setSize(queue.getSize() + 1)
                        return
                    else:
                        iterator = iterator.getNext()
                if iterator.getNext() is None:
                    aux.setNext(None)
                    iterator.setNext(aux)
                    queue.setSize(queue.getSize() + 1)
                    return


def getPQueue(queue):
    returnValue = 0

    if queue.getSize() > 0:
        returnValue = queue.getFirst().getVal()
        queue.setFirst(queue.getFirst().getNext())
        queue.setSize(queue.getSize() - 1)
    else:
        print("Queue is empty")
    return returnValue
