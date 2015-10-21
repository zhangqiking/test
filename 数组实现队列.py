class queue(object):
    def __init__(self):
        self.array=['#' for i in range(10)]
        self.front=0
        self.rear=-1
        self.capacity=10
        self.size=0
    def is_empty(self):
        return (self.size==0)

    def is_full(self):
        if self.size==10:
            return True

    def succ(self):
        if (self.rear+1==self.capacity):
            self.rear=0
        return self.rear

    def enqueue(self,tar):
        if (self.is_full()):
            return True
        else:
            self.rear=self.succ()
            self.array[self.rear+1]=tar
            self.rear+=1
            self.size+=1

    def dequeue(self):
        if (self.is_empty()):
            return "empry queue"
        else:
            q=self.array[self.front]
            self.array[self.front]='#'
            self.front+=1
            self.size-=1
        return q

    def show(self):
        print self.array

Q=queue()
for i in range(20):
   p= Q.enqueue(i)
   if p:
       print "full queue"
       break
Q.show()
'''print Q.size
for i in range(11):
   l= Q.dequeue()
   Q.show()
   print Q.size
'''


        

