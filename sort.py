import time
'''
class insert:
    def __init__(self,num):
        self.num=num
    def paixu(self):
        n=len(self.num)
        start_time=time.clock()
        for i in range(1,n):
            j=i-1
            temp=self.num[i]
            while j>=0 and temp<self.num[j]:
                self.num[j+1]=self.num[j]
                j=j-1
            self.num[j+1]=temp
        end_time=time.clock()
        t=end_time-start_time
        print "read: %f s" %(t)
        return self.num

m=insert([2,5,1,2,4])
print m.paixu()


class bubble_sort:
    def __init__(self,num):
        self.num=num
    def sort(self):
        start_time=time.clock()
        for i in range(1,len(self.num)):
            for j in range(len(self.num)-i):
                if self.num[j+1]<self.num[j]:
                    temp=self.num[j]
                    self.num[j]=self.num[j+1]
                    self.num[j+1]=temp
        end_time=time.clock()
        t=end_time-start_time
        print "read: %f s" %(t)
        return self.num

m=bubble_sort([2,5,1,2,4])
print m.sort()



