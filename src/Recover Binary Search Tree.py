# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        self.first,self.second,self.prevNode=None,None,None
        self.findSegments(A)
        x=self.first.val
        self.first.val=self.second.val
        self.second.val=x
        return[self.first.val,self.second.val]
    def findSegments(self,root):
        if(root==None):
            return
        self.findSegments(root.left)
        if(self.prevNode!=None):
            if(self.prevNode.val>root.val):
                if(self.first==None):
                    self.first=self.prevNode
                self.second=root
        self.prevNode=root
        self.findSegments(root.right)
