class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        if(len(A)<=1):
            return A
        i=len(A)-2
        
        while(i>=0):
            if(A[i]<A[i+1]):
                break
            i-=1
        if(i>=0):
            j=len(A)-1
            while(j>i):
                if(A[j]>A[i]):
                    break
                j-=1
            A[i],A[j]=A[j],A[i]
        b=sorted(A[i+1:len(A)])
        return (A[:i+1]+b)
