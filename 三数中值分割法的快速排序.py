# _*_ coding:utf-8 _*_
def swap(array,num1,num2):
    temp=array[num1]
    array[num1]=array[num2]
    array[num2]=temp

def median3(array,left,right):
    center=(left+right)/2
    '''
    if (array[left]>array[center]):
        swap(array,left,center)

    if (array[left]>array[right-1]):
        swap(array,left,right-1)

    if (array[center]>array[right-1]):
        swap(array,right-1,center)
        '''
    swap(array,center,right)
    return array[right]

def sub_sort(array,low,high):
    key=median3(array,low,high)
    h=high
    high=high-1
    while low<=high:
        while low<=high and array[high]>=key:
            high-=1
        while low<=high and array[low]<key:
            low+=1
        if (low<high):
            swap(array,low,high)

    swap(array,low,h)
    print array
    print low
    print high
    return low

def quick_sort(array,low,high):               #递归实现
    if low<high:
        key_index=sub_sort(array,low,high)
        quick_sort(array,low,key_index)       #对较小的部分排序
        quick_sort(array,key_index+1,high)    #对较大的部分排序
    return array

#sub_sort([8,2],0,1)
print quick_sort([2,8,0,5,7,4,9],0,5)


