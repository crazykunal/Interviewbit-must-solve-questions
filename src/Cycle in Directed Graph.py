import sys
sys.setrecursionlimit(5000)
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def __init__(self):
        self.graph = {}
        
    def isCyclic(self, node,visited,instack):
        visited[node] = True
        instack[node] = True
        for i in self.graph[node]:
            if(not visited[i]):
                if(self.isCyclic(i,visited,instack)):
                    return True
            elif instack[i]:
                return True
        instack[node] = False
        return False
        
    def solve(self, A, B):
        for i in range(1, A + 1):
            self.graph[i] = []
        for (src, dst) in B:
            self.graph[src].append(dst)
        
        visited = [False] * (A + 1)
        instack = [False] * (A + 1)
        
        for i in range(1, A + 1):
            if not visited[i]:
                if self.isCyclic(i,visited,instack):
                    return 1
        return 0
                    

