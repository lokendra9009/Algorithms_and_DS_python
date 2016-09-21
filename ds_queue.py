#Implementation of Queue in Python

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def sizeOfQueue(self):
        return len(self.items)

if __name__=='__main__':
    q=Queue()

    print q.isEmpty()

    q.enqueue(10)

    q.enqueue('abcd')

    print q.sizeOfQueue()

    print q.dequeue()

    print q.sizeOfQueue()
