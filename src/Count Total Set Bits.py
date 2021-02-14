class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, N):
        if(N==0):
            return 0
        p=0
        ans=0
        while((1<<p)<=N):
            p+=1
        p-=1
        ans+=p*(pow(2,p)//2)+(N-pow(2,p)+1)+self.solve(N-(pow(2,p)))
        ans%=1000000007
        return ans
