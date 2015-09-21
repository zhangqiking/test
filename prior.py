
class prior_list:
    def __init__(self):
        self.queue=[]
        self.length=0
        self.queue.insert(0,self.length)

    def cout(self):
        return self.length

    def is_empty(self):
        if self.cout()==0:
            return True
        else:
            return False

    def get_first(self):
        return self.queue[1]

    def pop(self):
        Min_num=self.queue[1]
        last_num=self.queue[self.length]
        i=1
        while i*2<=self.length:
            child=i*2
            if child!=self.length and self.queue[child+1]<self.queue[child]:
                child=child+1
            if last_num>self.queue[child]:
                self.queue[i]=self.queue[child]
            else:
                break
            i=child
        self.queue[i]=last_num
        self.queue.pop()


    def insert(self,tar):
        self.length+=1
        self.queue.insert(self.length,tar)
        i=len(self.queue)-1
        while self.queue[i/2]>tar and i>=2:
             self.queue[i]=self.queue[i/2]
             i=i/2
        self.queue[i]=tar

m=prior_list()
m.insert(4)
m.insert(5)
m.insert(1)
m.insert(9)
m.insert(23)
m.insert(12)
m.insert(0)
m.insert(35)

print m.queue
m.pop()
print m.queue

               




