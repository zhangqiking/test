class Node(object):
    def __init__(self,val,p=0):
        self.val=val
        self.next=p

class linkedlist(Node):
    def __init__(self):
        self.head=0

    def is_empty(self):
        p=self.head
        return (p.next==0)

    def is_last(self):
        p=self.head
        return (p.next==0)

    def initlist(self,data):
        self.head=Node(data[0])
        p=self.head
        for i in data[1:]:
            node=Node(i)
            p.next=node
            p=p.next

    def showlist(self):
        p=self.head
        while p!=0:
            print p.val
            p=p.next
    def getitem(self,tar):
        p=self.head
        if self.is_empty():
            return "linkedlist is empty"
        else:
            p=p.next
            while (p!=0 and p.val!=tar):
                p=p.next
            return p

    def delete_item(self,tar):
        p=self.find_previous(tar)

        if (not self.is_last()):
            temcell=p.next
            p.next=temcell.next

    def find_previous(self,tar):
        p=self.head
        while (p.next!=0 and p.next.val!=tar):
            p=p.next
        return p

    def insert(self,tar,position):
        p=self.find_previous(position).next
        temcell=Node(tar)
        temcell.next=p.next
        p.next=temcell




link=linkedlist()
link.initlist([1,5,2,3,6])
link.showlist()
'''
result=link.getitem(2)
print result.val
link.delete_item(2)
link.showlist()

link.insert(90,5)
link.showlist()
'''
p=link
print p




