# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        if A.val == B:
            return []
        res = [[]]
        q = [(A,0)]
        found_level = sys.maxsize
        while q:
            node,lev = q.pop(0)
            if lev > found_level:
                continue
            if lev == len(res):
                res.append([])
            if node.val == B:
                found_level = lev
            else:
                res[lev].append(node.val)
            if found_level == lev:
                continue
            if node.left:
                if not node.right or node.right.val != B:
                    q.append((node.left,lev+1))
            if node.right:
                if not node.left or node.left.val != B:
                    q.append((node.right,lev+1))
        return res[-1]
