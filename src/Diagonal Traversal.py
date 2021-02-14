# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        diagonalPrintMap = dict()
        res=[]
        self.diagonalPrintUtil(root, 0, diagonalPrintMap)
        for i in diagonalPrintMap:
            for j in diagonalPrintMap[i]:
                res.append(j)
        return res
    
    def diagonalPrintUtil(self,root, d, diagonalPrintMap):
        if root is None:
            return
        try :
            diagonalPrintMap[d].append(root.val)
        except KeyError:
            diagonalPrintMap[d] = [root.val]
     
        # Increase the vertical distance 
        # if left child
        self.diagonalPrintUtil(root.left, 
                            d+1, diagonalPrintMap)
         
        # Vertical distance remains 
        # same for right child
        self.diagonalPrintUtil(root.right, 
                               d, diagonalPrintMap)
