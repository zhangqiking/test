# _*_coding:utf-8 _*_

MAX_NUM=1000
v_num=6

Graph=[[0,6,1,5,MAX_NUM,MAX_NUM],
        [6,0,5,MAX_NUM,3,MAX_NUM],
        [1,5,0,5,5,4],
        [5,MAX_NUM,5,0,MAX_NUM,2],
        [MAX_NUM,3,6,MAX_NUM,0,6],
        [MAX_NUM,MAX_NUM,4,2,6,0],
      ]

u=[]                            #����Ѿ�ƥ��Ķ���
v=[]                            #��ʼ��Ϊ���ж��㼯��
t=[]                            #��ű�

def init():                     #��ʼ�����㼯��    
    i=0
    for i in range(v_num):
        v.append(i+1)


def list_sort(l):               #Ѱ�������е���Сֵ
    i=0
    min_val=l[0]
    while i<len(l):
        if min_val>l[i]:
            min_val=l[i]
            index=i
        i+=1
    return index

def prim():           
    i=0
    j=0
    close_edge={'u':-1,'v':-1}
    vertex_list=[]
    edge_list=[]
    length_u=len(u)
    length_v=len(v)

    while i<length_u:
        while j<length_v:
            temp=Graph[u[i]-1][v[j]-1]      #�����������ж��㵽��֪�������
            if temp>0:
                if temp<MAX_NUM:
                    close_edge={'u':u[i],'v':v[j]}
                vertex_list.append(close_edge)
                edge_distance_list.append(temp)
            j=j+1

        i=i+1
        j=0  
    

    min_index=list_sort(edge_distance_list)
    close_edge=vertex_list[min_index]
    u.append(close_edge['v'])
    del v[v.index(close_edge['v'])]


    return close_edge
   

if (__name__=="__main__"):    #��ʼ������
    init()
    start=2
    u.append(start)
    del v[start-1]            #u�ܼ���һ�������v�о�Ҫɾ����Ӧ�Ķ���
    while len(u)!=v_num:
        edge=prim()
        t.append(edge)
    print t
    print u



    
    








        
        

