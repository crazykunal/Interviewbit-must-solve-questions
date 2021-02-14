class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    res=0
    def solve(self, A, B):
        edges = [[] for i in range(A)]
        for edge in B:
            edges[edge[0]-1].append(edge[1]-1)
        visited = [False for i in range(A)]
        
        def dfs(curr):
            size = 1
            for neighbor in edges[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    tmp = dfs(neighbor)
                    if tmp%2:
                        size+=tmp
                    else:
                        self.res+=1
            return size
            
        dfs(0)
        return self.res
