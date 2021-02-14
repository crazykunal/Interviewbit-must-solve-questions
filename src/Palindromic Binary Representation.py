class Solution:
    # @param A : integer
    # @return an integer
    def revBin(self,val):
        rev=0
        while(val>0):
            rev<<=1
            rev|=val&1
            val=val>>1
        return rev
    def solve(self, A):
        len1=1
        count=1
        while(count<A):
            len1+=1
            count+=1<<((len1-1)//2)
        count-=1<<((len1-1)//2)
        nextbit=A-count-1
        ans=(1<<(len1-1))
        ans|=(nextbit<<(len1//2))
        val=ans>>(len1//2)
        rev=self.revBin(val)
        ans|=rev
        return ans
