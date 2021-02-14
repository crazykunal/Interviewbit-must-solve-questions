# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head==None:
            return head
        
        # Add new nodes into the hashmap
        # with original nodes as keys and
        # new nodes as values.
        Map = dict()
        cur = head
        while cur!=None:
            Map[cur] = RandomListNode(cur.label)
            cur = cur.next
        
        # Traverse the linked list and
        # add the pointers for values.
        cur = head
        while cur!=None:
            temp1 = Map[cur]
            temp2 = Map.get(cur.next, None)
            temp1.next = temp2
            cur = cur.next
        
        # Add the random pointers in same
        # way of the original linked list.
        cur = head
        while cur!=None:
            temp1 = Map[cur]
            temp2 = Map.get(cur.random, None)
            temp1.random = temp2
            cur = cur.next
        
        return Map[head]

