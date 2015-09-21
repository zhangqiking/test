import time

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


class Quick_sort:
    def __init__(self,num):
        self.num=num
    def sort(self):
        start_time=time.clock()
        for i in range(len(self.num)-1):
            index=i
            for j in range(i+1,len(self.num)):
                if self.num[j]<self.num[index]:
                    temp=self.num[i]
                    self.num[i]=self.num[j]
                    self.num[j]=temp
        end_time=time.clock()
        t=end_time-start_time
        print "read: %f s" %(t)
        return self.num

m=Quick_sort([2,5,1,2,4,56,23,8,7,53,7,0,8,9])
print m.sort()


def Merge_sort(num,low,mid,high):
    i=low
    j=mid
    k=0
    array=[]
    while i<mid and j<=high:

        if (num[i]<=num[j]):
            array.append(num[i])
            i=i+1
            k=k+1
        else:
            array.append(num[j])
            j=j+1
            k=k+1
    while (i<mid):
        array.append(num[i])
        i=i+1
        k=k+1
    while (j<=high):
        array.append(num[j])
        j=j+1
        k=k+1

    for m in range(len(array)):
        num[m]=array[m]
    print num


n=[2,5,6,2,4,56]
Merge_sort(n,0,len(n)/2,len(n)-1)


def Hill_sort(num):
    gap=len(num)/2
    while (gap>=1):
        for i in range(gap,len(num)):
            j=i-gap
            temp=num[i]
            while j>=0:
                if temp<num[j]:
                    t=num[j]
                    num[j]=num[j+gap]
                    num[j+gap]=t
                j=j-gap
        gap=gap/2
    return num

n=[2,5,6,1,4,56,0,7,12,43,23,10]
print Hill_sort(n)





















                    





