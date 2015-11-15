# _*_coding:utf-8 _*_

def hash_fun(val,table_size):
    return val % table_size

def hash_openadd(data):      #开放地址法处理散列冲突
    table = {}
    table_size = len(data)
    for i in range(table_size):
        j=1
        key = hash_fun(data[i],table_size)
        while table.has_key(key):
            key =(hash_fun(data[i],table_size)+j) % table_size
            j=j+1
        table[key] = data[i]

    return table

def hash_sep(data):         #分离连接法处理散列冲突
    table = {}
    table_size = 13
    data_num = len(data)
    
    for i in range(data_num):
        key = hash_fun(data[i],table_size)
        if not table.has_key(key):
            table[key]=[]
        table[key].append(data[i])

    return table



 
m=[13,15,24,6,9,0]
table = hash_sep(m)
n=0
for i in table:      #计算字典中键值的个数
    n=n+1
print n


            
    

