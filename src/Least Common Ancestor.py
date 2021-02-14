# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    f1 = False
    f2 = False
    def lca(self, A, val1, val2):
        if not self.check(A, val1):
            return -1
        if not self.check(A, val2):
            return -1
        return self.find(A, val1, val2)
    def check(self, A, val):
        if not A:
            return False
        if A.val == val:
            return True
        return self.check(A.left, val) or self.check(A.right, val)
    def find(self, A, val1, val2):
        if not A:
            return -1
        if A.val == val1 or A.val == val2:
            return A.val
        left = self.find(A.left, val1, val2)
        right = self.find(A.right, val1, val2)
        
        if left>0 and right > 0:
            return A.val
        
        if left>0:
            return left
        return right
