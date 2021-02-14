class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        import sys
        res=[]
        s=-1
        e=-1
        for i in range(len(A)-1):
            if(A[i]>A[i+1]):
                s=i
                break
        if(s==-1):
            res.append(s)
            return res
        for i in range(len(A)-1,s-1,-1):
            if(A[i]<A[i-1]):
                e=i
                break
        max1=-sys.maxsize
        min1=sys.maxsize
        for i in range(s,e+1):
            max1=max(max1,A[i])
            min1=min(min1,A[i])
        for i in range(s):
            if(A[i]>min1):
                s=i
                break
        for i in range(len(A)-1,e,-1):
            if(A[i]<max1):
                e=i
                break
        res.append(s)
        res.append(e)
        return res
