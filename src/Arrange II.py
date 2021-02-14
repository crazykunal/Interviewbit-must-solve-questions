class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, B):
        n=len(A)
        dp=[[0 for i in range(B)] for j in range(n)]
        if B>n:
            return -1
        w=0
        b=0
        for i in range(n):
            if A[i]=='W':
                w+=1
            else:
                b+=1
            dp[i][0]=w*b
        for i in range(1,B):
            for j in range(n):
                if i>j:
                    dp[j][i]=-1
                else:
                    w=0
                    b=0
                    m=sys.maxsize
                    for k in range(j-1,-1,-1):
                        if A[k+1]=='W':
                            w+=1
                        else:
                            b+=1
                        if dp[k][i-1]+w*b>=0:
                            m=min(m,dp[k][i-1]+w*b)
                    dp[j][i]=m
        return dp[n-1][B-1]
