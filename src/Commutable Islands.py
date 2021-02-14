class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        from collections import defaultdict
        import heapq
        connected = {1}
        adj = defaultdict(list)
    
        for u, v, w in B:
            adj[u].append( (w,  v))
            adj[v].append( ( w, u))
        pending = adj[1][:]
        heapq.heapify(pending)
        cost = 0
        while len(pending) > 0:
            w, u = heapq.heappop(pending)
            if u in connected:
                continue
            connected.add(u)
            cost += w
            for ww, v in adj[u]:
                if v not in connected:
                    heapq.heappush(pending,  (ww, v) )
        return cost

