
from asyncio.windows_events import NULL
from dis import dis
from pickle import FALSE, TRUE
from turtle import distance


WHITE = 0
GRAY = 1
BLACK = 2

def belongs( a, b) :
    if b == NULL :
        return 0
    for i in b :
        if a.name == i.name :
            return 1
    return 0

class node :
    def __init__(self, name, M):
        self.name = name
        self.parent = NULL
        self.distance = NULL
        self.adj = []
        for i, v in enumerate(M[name, :]) :
            if v != 0 :
                self.adj.append((i, v))
        """print("Node constructor successfully called")"""
    
    def SetDistance(self, distance) :
        self.distance = distance
    def GetDistance(self):
        return self.distance


class Graph:
    
    def __init__(self,M):
        self.Mat = M
        self.N = M.shape[0]
        self.nodes = []
        for i in range(0, self.N):
            e = node(i , self.Mat)
            self.nodes.append(e)
        """print("Graph Constructor successfully called")"""
        
        
    """def getParent(self,index):
        return self.parent[index]
        
    def getColor(self,index):
        return self.color[index]
    
    def setParent(self,index,P):
        self.parent[index] = P
        
    def setColor(self,index,color):
        self.color[index] = color"""
        
    def getAdj(self, index):
        adj=[]
        for i,v in enumerate(self.Mat[index,:]):
            if v!=0:
                adj.append((i, v))
        return adj
    
    

class UCS:
    
    def __init__(self,G,source, goal):
        self.goal = goal
        self.G = G
        self.source = source
        self.Q = []
        self.path = []
        self.visited = []
        """print("UCS constructor successfully called")"""
        
    def traverse(self):
        u = self.G.nodes[self.source]
        u.parent = NULL
        u.distance = 0
        self.Q.append(u)
        """print("UCS traversal successfully called")"""
        while self.Q :
            u = self.Q.pop()
            self.visited.append(u)
            print(u.name, u.distance)
            for i in u.adj:
                v = self.G.nodes[i[0]]
                d = u.distance + i[1]
                """if v in self.Q :"""
                if belongs(v , self.Q)  == 1 or belongs(v, self.visited) == 1:
                    if d < v.distance :
                        v.distance = d
                        v.parent = u.name
                
                else :
                    v.distance = d
                    v.parent = u.name
                    self.Q.append(v)
        """print("UCS traversal successfully finished")"""


    def printpath(self):
        u = self.G.nodes[self.goal]
        cost = u.distance
        while u.parent != NULL :
            self.path.append(u.name)
            print(u.parent)
            u = self.G.nodes[u.parent]
        print("Path : ", self.path )
        print("Total Cost : ", cost)
        
        
             
import numpy as np

M = np.array([[0,2,3,0,0],
              [2,0,0,1,0],
              [3,0,0,4,2],
              [0,1,4,0,8],
              [0,0,2,8,0]])

G = Graph(M)
UCS = UCS(G, 0, 4)
UCS.traverse()
UCS.printpath()