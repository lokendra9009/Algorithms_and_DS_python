#LinkedList implementation in Python 2.7

#create a node data type to hold the data for a linkedlist

class Node(object):
    def __init__(self,d=None,n=None):
        self.data=d
        self.next_node=n

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self,d):
        self.data=d

    def set_next(self,n):
        self.next_node=n

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0

    def get_size(self):
        return self.size

    def add_data(self,element):
        temp=Node(element,self.head)
        self.head=temp
        self.size+=1

    def find_data(self,d):
        this_node=self.head
        while (this_node!=None):
            if this_node.get_data()==d:
                return d
            else:
                this_node=this_node.get_next()
        return None

    def remove_data(self,d):
        this_node=self.head
        prev_node=None
        while (this_node!=None):
            if this_node.get_data()==d:
                if prev_node!=None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head=this_node.get_next()
                self.size-=1
                return True
            else:
                prev_node=this_node
                this_node=this_node.get_next()
    def display_list(self):
        this_node=self.head
        while (this_node!=None):
            print this_node.get_data()
            this_node=this_node.get_next()


if __name__=='__main__':
    list1=LinkedList()
    list1.add_data(5)
    list1.add_data('Hello')
    list1.add_data('100')
    print list1.get_size()
    #print list1.find_data('Hello')
    list1.display_list()
    
        
