# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0
        
        

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val
        
        
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
