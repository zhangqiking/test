# _*_ coding:utf-8 _*_

class Btree(object):
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None


def create_tree():
    temp=input()
    T=Btree()
    if temp=='#':
        T=None
    else:
        T.val=temp
        T.left=create_tree()
        T.right=create_tree()
    return T

def insert(T,tar):
        if (T==None):
             T=Btree()
             T.val=tar
             T.left=None
             T.right=None
        else:
            if (tar<T.val):
               T.left=insert(T.left,tar)
            else:
               T.right=insert(T.right,tar)
        return T 

def delete(T,tar):
    if (T==None):
        return None
    else:
        if (tar<T.val): 
            T.left=delete(T.left,tar)     #调整删除之后的父子节点关系
        elif (tar>T.val):
            T.right=delete(T.right,tar)
        else:
            if (T.left!=None and T.right!=None):
                tempcell=find_min(T.right)
                T.val=tempcell.val
                T.right=delete(T.right,tar)
            else:
                tempcell=T
                if (T.left==None):
                    T=T.right
                elif (T.right==None):
                    T=T.left
                del tempcell
    return T


def find(T,tar):
    if (T==None):
        return None
    if (tar<T.val):
        return find(T.left,tar)
    elif (tar>T.val):
        return find(T.right,tar)
    else:
        return T

def find_min(T):
    if (T==None):
        return None
    elif (T.left==None):
        return T
    else:
        return find_min(T.left)

def find_max(T):
    if (T==None):
        return None
    elif (T.right==None):
        return T
    else:
        return find_max(T.right)

def in_order(T):
    if (T is not None):
        in_order(T.left)
        print T.val
        in_order(T.right)

def end_order(T):
    if (T is not None):
        end_order(T.right)
        end_order(T.left)
        print T.val

def pre_order(T):
    if(T is not None):
        print T.val
        pre_order(T.left)
        pre_order(T.right)


    
       


t=create_tree()
insert(t,1)
insert(t,3)
insert(t,4)

pre_order(t)
print '----------'
in_order(t)
print '----------'
end_order(t)
print '----------'
delete(t,3)
pre_order(t)
    

