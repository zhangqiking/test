#-*- coding: utf-8 -*-
import random

v = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

#�б���б��ʾ�ɶ�ά����


def display(v, score):
    
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[0][0], v[0][1], v[0][2], v[0][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[1][0], v[1][1], v[1][2], v[1][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[2][0], v[2][1], v[2][2], v[2][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[3][0], v[3][1], v[3][2], v[3][3]))
        print 'Total score: ', score


def init(v):
   
    for i in range(4):
        v[i] = [random.choice([0, 0, 0, 2, 2, 4]) for x in range(4)]
  
def align(vList, direction):
   
  
    # �Ƴ��б��е�0
    for i in range(vList.count(0)):
        vList.remove(0)
    # ���Ƴ���0
    zeros = [0 for x in range(4 - len(vList))]
    # �ڷ�0���ֵ�һ�ಹ��0
    if direction == 'left':
        vList.extend(zeros)
    else:
        vList[:0] = zeros
      
def addSame(vList, direction):
    '''���б������ͬ�����ڵ��������, �ҵ����������ķ���True�����򷵻�False,ͬʱ���������ӵķ���
      
    direction == 'left':����������ң��ҵ���ͬ�����ڵ��������֣�������ַ������Ҳ�������0
    direction == 'right':�������Ҳ��ң��ҵ���ͬ�����ڵ��������֣��Ҳ����ַ��������������0
    '''
    score = 0
    if direction == 'left':
        for i in [0, 1, 2]:
            if vList[i] == vList[i+1] != 0: 
                vList[i] *= 2
                vList[i+1] = 0
                score += vList[i]
                return {'bool':True, 'score':score}
    else:
        for i in [3, 2, 1]:
            if vList[i] == vList[i-1] != 0:
                vList[i-1] *= 2
                vList[i] = 0
                score += vList[i-1]
                return {'bool':True, 'score':score}
    return {'bool':False, 'score':score}
  
def handle(vList, direction):
    
    totalScore = 0
    align(vList, direction)
    result = addSame(vList, direction)
    while result['bool'] == True:
        totalScore += result['score']
        align(vList, direction)
        result = addSame(vList, direction)
    return totalScore
      
  
def operation(v):
    '''�����ƶ��������¼������״ֵ̬������¼�÷�
    '''
    totalScore = 0
    GameOver = False
    direction = 'left'
    op = input('operator:')
    if op in ['a', 'A']:  # �����ƶ�
        direction = 'left'
        for row in range(4):
            totalScore += handle(v[row], direction)
    elif op in ['d', 'D']: # �����ƶ�
        direction = 'right'
        for row in range(4):
            totalScore += handle(v[row], direction)
    elif op in ['w','W']:
        direction='left'

        for col in range(4):
            #�������һ�и��Ƶ���һ���б�
            vlist=[v[row][col] for row in range(4)]
            totalScore+=handle(vlist,direction)

            for row in range(4):
                v[row][col]=vlist[row]
    elif op in ['s','S']:
        direction='right'
        for col in range(4):
            vlist=[v[row][col] for row in range(4)]
            totalScore+=handle(vlist,direction)
            for row in range(4):
                v[row][col]=vlist[row]
    else:
        print('Invalid input,please try again')
        return {'gameover':GameOver,'score':totalScore}
   
    #ͳ�ƿհ�������Ŀ

    N=0
    for q in v:
        N+=q.count(0)

    if N==0:
        GameOver=True
        return {'gameover':GameOver,'score':totalScore}

    num=random.choice([2,2,2,4])
    
    k=random.randrange(1,N+1)                       # ���������k����һ��������2��4�������k���հ�����
    n=0
    for i in range(4):
        for j in range(4):
            if v[i][j]==0:
                n+=1
                if n==k:
                    v[i][j]=num
                    break
    return {'gameover':GameOver,'score':totalScore}



#������


init(v)
score=0
print('input direction')

while True:
    display(v,score)
    result=operation(v)
    if result['gameover']==True:
        print('Game Over')
        print('your score:',score)
    else:
        score+=result['score']
        if score>=2048:
            print('you win')
            print('your score:',score)


