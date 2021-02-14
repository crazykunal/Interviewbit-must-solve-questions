class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, s):
        if not s: return -1
        n=len(s)
        cuts=[i for i in range(n)]
        isPalindrome = [[False for _ in range(n)] for _ in range(n)] 
        for i in range(n):
            isPalindrome[i][i]=True
            for j in range(i+1):
                if s[i]==s[j] and (i-j<2 or isPalindrome[j+1][i-1]==True ):
                    if j==0:
                        cuts[i]=0
                    else:
                        isPalindrome[j][i]=True
                        cuts[i]=min(cuts[i],cuts[j-1]+1)
        return cuts[n-1]
