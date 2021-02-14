class Solution:
    # @param A : string
    # @return an integer
    MOD = 1003
    def cnttrue(self, s):
        n=len(s)
        dp=[[[-1 for k in range(2)] for j in range(n)] for i in range(n)]
        return self.parenthesis_count(s, 0, n - 1, 1,dp)%1003
    def parenthesis_count(self,s, i, j, isTrue,dp):
        if (i > j):
            return false
        if (i == j):
            if (isTrue == 1):
                return s[i] == 'T'
            else:
                return s[i] == 'F'
        if (dp[i][j][isTrue] != -1):
            return dp[i][j][isTrue]
        ans=0
        for k in range(i+1,j,2):
            if(dp[i][k - 1][1]==-1):
                leftT = self.parenthesis_count(s, i, k - 1, 1,dp)
            else:
                leftT = dp[i][k - 1][1]
            if(dp[k + 1][j][1] == -1):
                rightT = self.parenthesis_count(s, k + 1, j, 1,dp)
            else:
                rightT = dp[k + 1][j][1]
            if(dp[i][k - 1][0] == -1):
                leftF = self.parenthesis_count(s, i, k - 1, 0,dp)
            else:
                leftF = dp[i][k - 1][0]
            if(dp[k + 1][j][0] == -1): 
                rightF = self.parenthesis_count(s, k + 1, j, 0,dp)
            else:
                rightF = dp[k + 1][j][0]
            if(s[k] == '&'):
                if(isTrue == 1):
                    ans += leftT * rightT
                else:
                    ans += leftF * rightF + leftT * rightF+ leftF * rightT
            elif (s[k] == '|'):
                if (isTrue == 1):
                    ans += leftT * rightT + leftT * rightF+ leftF * rightT
                else:
                    ans = ans + leftF * rightF
            elif (s[k] == '^'):
                if (isTrue == 1):
                    ans = ans + leftF * rightT + leftT * rightF
                else:
                    ans = ans + leftT * rightT + leftF * rightF
            dp[i][j][isTrue] = ans
        return ans
            
            
            
            
            
            
            
            
            
            

    
        

    
                  
