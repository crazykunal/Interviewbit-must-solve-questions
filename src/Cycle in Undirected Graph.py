class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def dfs(self,node,parent,visited):
        
        visited[node]=True
        
        for i in self.graph[node]:
            
            if(not visited[i]):
                if self.dfs(i,node,visited):
                    return True
            elif(parent!=i): 
                return True
    
        return False
        
    def solve(self, v, a):
        from collections import defaultdict
        self.graph=defaultdict(list)
        visited={}
        
        for i in a:
            self.graph[i[0]].append(i[1])
            self.graph[i[1]].append(i[0])
            visited[i[0]]=False
            visited[i[1]]=False
            
        for i in visited.keys():
            #print(i)
            if visited[i]==False:
                if self.dfs(i,-1,visited):
                    return 1
        return 0
