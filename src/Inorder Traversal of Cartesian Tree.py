# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        s=0
        e=len(A)-1
        return self.helper(A,s,e)
    def helper(self,A,s,e):
        if(s>e):
            return None
        i=self.max1(A,s,e)
        root=TreeNode(A[i])
        if(s==e):
            return root
        root.left=self.helper(A,s,i-1)
        root.right=self.helper(A,i+1,e)
        return root
    def max1(self,A,s,e):
        m=A[s]
        maxind=s
        for i in range(s+1,e+1):
            if(A[i]>m):
                m=A[i]
                maxind=i
        return maxind
