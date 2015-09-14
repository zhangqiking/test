import time

class insert:
    def __init__(self,num):
        self.num=num
    def paixu(self):
        n=len(self.num)
        start_time=time.clock()
        for i in range(n-1):
            for j in range(n-1):
                temp=self.num[j+1]
                if temp<self.num[j]:
                    self.num[j+1]=self.num[j]
                    self.num[j]=temp
        end_time=time.clock()
        t=end_time-start_time
        print "read: %f s" %(t)
        return self.num

m=insert([2,5,1,4])
print m.paixu()

                    
                    


