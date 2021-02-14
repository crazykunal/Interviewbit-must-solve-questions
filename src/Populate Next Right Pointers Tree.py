# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        node = root
        while node:
            lstart = node
            foundFirst = False
            prev = None
            while lstart:
                if lstart.left : 
                    if not foundFirst:
                        foundFirst = True
                        node = lstart.left 
                        prev= lstart.left
                    else:
                        prev.next = lstart.left
                        prev = lstart.left
                if lstart.right :
                    if not foundFirst :
                        foundFirst = True
                        node = lstart.right 
                        prev= lstart.right
                    else:
                        prev.next = lstart.right
                        prev = lstart.right
                lstart = lstart.next
            if not foundFirst:
                node = None
        return root
        
