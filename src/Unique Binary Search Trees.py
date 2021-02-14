# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode 
    def generateTrees(self, n):
        def gen_trees(s, e):
            ret_list=[]
            if s>e:
                return [None]
            for i in range(s, e + 1):
                list_left = gen_trees(s, i - 1)
                list_right = gen_trees(i + 1, e)
                for left in list_left:
                    for right in list_right:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ret_list.append(root)
            return ret_list
    
        if n == 0:
            return []
        return gen_trees(1, n)
