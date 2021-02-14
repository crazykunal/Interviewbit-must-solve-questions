class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, arr, k):
        from collections import defaultdict 
        mp = defaultdict(lambda:0) 
        dist_count = 0
        n=len(arr)
        res=[]
        for i in range(k): 
            if mp[arr[i]] == 0: 
                dist_count += 1
            mp[arr[i]] += 1
        res.append(dist_count) 
        for i in range(k, n): 
            if mp[arr[i - k]] == 1: 
                dist_count -= 1
            mp[arr[i - k]] -= 1
            if mp[arr[i]] == 0: 
                dist_count += 1
            mp[arr[i]] += 1
            res.append(dist_count) 
        return res
