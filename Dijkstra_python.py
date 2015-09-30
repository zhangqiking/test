'''
Dijkstra最短路径算法
S= [{'index': 1, 'val': 0}, {'index': 3, 'val': 15}, {'index': 2, 'val': 25}, {'index': 6, 'val': 30}, {'index': 5, 'val': 40}, {'index': 4, 'val': 50}] 
dist= [0, 25, 15, 50, 40, 30] 

'''

debug = 0
MAX_NUM = 10000
v_num = 6

#S 放 最短路径节点添加过程
S = []  #[{'index':1 , 'val' : 0 }, ····]

#dist 放各个步骤临时dist值

##########################################
dist = []
edge = [
      [0 , 30 , 15 ,MAX_NUM , MAX_NUM , MAX_NUM ],
      [5 , 0 , MAX_NUM , MAX_NUM ,20 ,30 ],
      [MAX_NUM , 10 , 0 , MAX_NUM ,MAX_NUM , 15],
      [MAX_NUM , MAX_NUM , MAX_NUM , 0 ,MAX_NUM , MAX_NUM],
      [MAX_NUM , MAX_NUM , MAX_NUM , 30 ,10 ,0 ]
]

###########################################

def init (start) :
      if (debug):
             print("[init]")
      s.append({'index':start , 'val': 0})
      i = 0
      while ( i < v_num ):
            dist.append(edge[start - 1][i])
            i = i + 1

def v_in_s(v) :
      i = 0 
      while ( i < len(S)) :
            if ( v == S[i]['index']):
                  return "YES"
            i = i + 1
      return "NO"

def get_min() :
      if (debug):
            print("[get_min]")
      if (len(dist) < 1 ) :
            return {'index' : -1 ,'val' : 0 }
      i = 0
      min_val = MAX_NUM
      min_index = 0
      while ( i < len(dist)):
            if(v_in_s(i + 1) == "NO") :
                  if (dist[i] < MAX_NUM and dist[i] > 0 and min_val > dist[i]) :
                        min_val = dist[i]
                        min_index = i
            i = i + 1
      return {'index' : min_index + 1 , 'val' : min_val }

def update_dist() :
      tmp_index = S[len(S) -1]['index']
      tmp_val = S[len(S) - 1]['val']
      if (debug) :
            print("[update_dist]" , "tmp_index=",tmp_index , ";tmp_val=",tmp_val)
      i = 0
      while ( i < v_num ) :
            if ( v_in_s(i + 1) == "NO") :
                  i_dist = tmp_val + edge[tmp_index - 1][i]
                  if (debug) :
                        print(" i = ", i ," i_dist = " , i_dist)
                  if(dist[i] > i_dist) :
                        dist[i] = i_dist
            i = i + 1
      if (debug) :
            print ("after update dist : dist = " , dist)

def process() :
      if (debug) :
            print("[process]")
      i = 0
      S_len = len(S)
      while (v_num != S_len and i < v_num ):
            min_vertex = get_min()
            if(debug) :
                  print ("i = " , i , ";min_vertex = ", min_vertex)
                  print ("len(S) = " , len(S),"; S = ", S)
            if(min_vertex['index'] > 0 ) :
                  if (debug) :
                        print("---BFFORE append :  len(S) = ", len(S),";S = ",S)
                  S.append(min_vertex)
                  if (debug) :
                        print("====after append : len(S) = ", len(S) ,";S = ",S)
                  update_dist()

            i = i + 1
            S_len = len (S)

def py_Dijkstra (start) :
      init (start)
      print("初始条件：\n", "\t start = " , start ,"\n\t S = ", S ,"\n\t dist = ", dist)
      process()
      print ("结果 : \n","\t S = " ,S ,"\n\t dist = ", dist)

if (__name__ == "__main__"):
      py_Dijkstra(1)
            
                  
            
            
            
