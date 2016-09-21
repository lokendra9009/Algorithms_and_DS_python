#Stack Implementation in Python

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items==[]
    def topOfStack(self):
        return len(self.items)
    def topElementOfStack(self):
        return self.items[-1]


if __name__ == "__main__":
    stck = Stack()

    stck.push(10)
    stck.push(20)
    stck.push(30)

    print stck.topOfStack()
    print stck.topElementOfStack()

    stck.pop()
    
    print stck.topOfStack()
    print stck.topElementOfStack()
