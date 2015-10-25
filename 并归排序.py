#_*_ coding:utf-8 _*_

'''def merge(array,temparray,left,center,right):
    leftend=center-1
    nums=right-left+1
    i=0
    while (left<=leftend and center<=right):
        if (array[left]<array[center]):
            temparray.append(array[left])
            left+=1
        else:
            temparray.append(array[center])
            center+=1
    while (left<=leftend):
        temparray.append(array(left))
        left+=1
    while (center<=right):
        temparray.append(array[center])
        center+=1
    print temparray
    while (i<nums):
        array[right]=temparray[right]
        right-=1
        i+=1
    

def Msort(array,temparray,left,right):
    if(left<right):
        center=(left+right)/2
        Msort(array,temparray,left,center)
        Msort(array,temparray,center+1,right)
        merge(array,temparray,left,center+1,right)
    return array

def MergeSort(array):
    length=len(array)

def merge(array,left,center,right):
    if center==0:
        center=1
    leftend=center-1
    nums=right-left+1
    i=0
    temparray=[]
    while (left<=leftend and center<=right):
        if (array[left]<array[center]):
            temparray.append(array[left])
            left+=1
        else:
            temparray.append(array[center])
            center+=1
    while (left<=leftend):
        temparray.append(array[left])
        left+=1
    while (center<=right):
        temparray.append(array[center])
        center+=1
    print temparray
    while (i<nums):
        array[right]=temparray[right]
        right-=1
        i+=1
    print array


def Msort(array,left,right):
    if(left<right):
        center=(left+right)/2
        Msort(array,left,center)
        Msort(array,center+1,right)
        merge(array,left,center+1,right)
array=[1,3,2,5,0]
Msort(array,0,4)
print array                                         
'''  

def merge(array,temparray,left,center,right):        #分析只有两个元素的基准情况，当只有两个元素是，两边自然是已排序状态
    tmppos=left
    if center==0:
        center=1
    leftend=center-1
    nums=right-left+1
    i=0
    while (left<=leftend and center<=right):
        if (array[left]<array[center]):
            temparray[tmppos]=array[left]
            left+=1
            tmppos+=1
        else:
            temparray[tmppos]=array[center]
            center+=1
            tmppos+=1
    while (left<=leftend):
        temparray[tmppos]=array[left]
        left+=1
        tmppos+=1
    while (center<=right):
        temparray[tmppos]=array[center]
        center+=1
        tmppos+=1
    print temparray
    while (i<nums):
        array[right]=temparray[right]
        right-=1
        i+=1
    print array


def Msort(array,temparray,left,right):
    if(left<right):
        center=(left+right)/2
        Msort(array,temparray,left,center)
        Msort(array,temparray,center+1,right)
        merge(array,temparray,left,center+1,right)

array=[1,3,10,2,67,5,0]
temp=[0,0,0,0,0,0,0]
Msort(array,temp,0,6)
print array 

