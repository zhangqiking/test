#-*- coding: utf-8 -*-
import random

v = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

#列表的列表表示成二维数组


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
   
  
    # 移除列表中的0
    for i in range(vList.count(0)):
        vList.remove(0)
    # 被移除的0
    zeros = [0 for x in range(4 - len(vList))]
    # 在非0数字的一侧补充0
    if direction == 'left':
        vList.extend(zeros)
    else:
        vList[:0] = zeros
      
def addSame(vList, direction):
    '''在列表查找相同且相邻的数字相加, 找到符合条件的返回True，否则返回False,同时还返回增加的分数
      
    direction == 'left':从右向左查找，找到相同且相邻的两个数字，左侧数字翻倍，右侧数字置0
    direction == 'right':从左向右查找，找到相同且相邻的两个数字，右侧数字翻倍，左侧数字置0
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
    '''根据移动方向重新计算矩阵状态值，并记录得分
    '''
    totalScore = 0
    GameOver = False
    direction = 'left'
    op = input('operator:')
    if op in ['a', 'A']:  # 向左移动
        direction = 'left'
        for row in range(4):
            totalScore += handle(v[row], direction)
    elif op in ['d', 'D']: # 向右移动
        direction = 'right'
        for row in range(4):
            totalScore += handle(v[row], direction)
    elif op in ['w','W']:
        direction='left'

        for col in range(4):
            #将矩阵的一列复制到另一个列表
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
   
    #统计空白区域数目

    N=0
    for q in v:
        N+=q.count(0)

    if N==0:
        GameOver=True
        return {'gameover':GameOver,'score':totalScore}

    num=random.choice([2,2,2,4])
    
    k=random.randrange(1,N+1)                       # 产生随机数k，上一步产生的2或4将被填到第k个空白区域
    n=0
    for i in range(4):
        for j in range(4):
            if v[i][j]==0:
                n+=1
                if n==k:
                    v[i][j]=num
                    break
    return {'gameover':GameOver,'score':totalScore}



#主程序


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


