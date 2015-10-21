# -*- coding:utf-8 -*-
#栈的链表实现

class Node(object):
    def __init__(self,p=0):
        self.val=None
        self.next=p

class stack(Node):
    def __init__(self):
        self.head=0

    def create_stack(self):
        self.head=Node()
        self.head.next=0

    def is_empty(self):
        return (self.head.next==0)

    def make_empty(self):
        while (not self.is_empty()):
            self.pop()

    def push(self,tar):
        tempcell=Node()
        tempcell.val=tar
        tempcell.next=self.head.next
        self.head.next=tempcell

    def pop(self):
        if (self.is_empty()):
            return "empty stack"
        else:
            firstcell=self.head.next
            self.head.next=firstcell.next
        return firstcell.val

s=stack()
s.create_stack()
for i in range(5):
    s.push(i)
for i in range(5):
    print s.pop()










 
