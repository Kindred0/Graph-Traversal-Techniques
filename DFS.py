WHITE = 0
GRAY = 1
BLACK = 2

class Graph:
    
    def __init__(self,M):
        self.Mat = M
        self.N = M.shape[0]
        self.parent = [None for _ in range(self.N)]
        self.color = [None for _ in range(self.N)]
        
        
    def getParent(self,index):
        return self.parent[index]
        
    def getColor(self,index):
        return self.color[index]
    
    def setParent(self,index,P):
        self.parent[index] = P
        
    def setColor(self,index,color):
        self.color[index] = color
        
    def getAdj(self, index):
        adj=[]
        for i,v in enumerate(self.Mat[index,:]):
            if v!=0:
                adj.append(i)
        return adj
    
    

class DFS:
    
    def __init__(self,G,source):
        
        self.G = G
        self.source = source
        self.Q = []
        self.result = []

    def traversal(self, u):
        for v in self.G.getAdj(u) :
            if self.G.getColor(v) == WHITE :
                self.G.setColor(v, GRAY)
                self.G.setParent(v, u)
                self.traversal(v)
        self.G.setColor(u, BLACK)
        self.result.append(u)   
    
    def traverse(self):
    
        for i in range(self.G.N):
            self.G.setColor(i,WHITE)
            self.G.setParent(i,None)
            
        self.G.setColor(self.source,GRAY)
        self.traversal(self.source)
            
    def printResult(self):
        for u in self.result:
            print(u,end=' ')
        print('')
            
    def printLevel(self,curr,depth):
        if curr == None:
            return;
        for i in range(1,depth):
            print("│   ",end='')
        if depth > 0:
            print("|___",end='')
        print(curr);

        for child in [i for i,x in enumerate(self.G.parent) if x== curr]:
            self.printLevel(child, depth + 1);
        

import numpy as np

M = np.array([[0,1,1,0,0],
              [1,0,0,1,0],
              [1,0,0,1,1],
              [0,1,1,0,1],
              [0,0,1,1,0]])

G = Graph(M)
bfs = DFS(G,3)
bfs.traverse()
bfs.printResult()
bfs.printLevel(1,0)