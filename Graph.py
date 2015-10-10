# -*- coding:utf-8 -*-

'''
图的数据结构实现，利用字典和列表实现邻接表
'''
class Graph:
    def __init__(self,graph):
        self.graph=graph


    def find_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if not self.graph.has_key(start):
            return None
        for node in self.graph[start]:
            if node not in path:
                newpath=self.find_path(node,end,path)
                if newpath:
                    return newpath
        return None

    def find_all_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if not self.graph.has_key(start):
            return None
        paths=[]
        for node in self.graph[start]:
            if node not in path:
                newpaths=self.find_all_path(node,end,path)
                for newpath in newpaths:
                    paths.append(newpath)        
        return paths

    def find_shortest_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if not self.graph.has_key(start):
            return None
        shortest=None
        for node in self.graph[start]:
            if node not in path:
                newpath=self.find_shortest_path(node,end,path)
                if newpath:
                    if not shortest or len(newpath)<len(shortest):
                        shortest=newpath
        return shortest

            


        


'''
例程
'''

graph={'a':['b','c'],
         'b':['d','c'],
         'c':['d'],
         'd':['c'],
         'e':['f'],
         'f':['c']
        }
G=Graph(graph)

p=G.find_shortest_path('a','d')

print p
