# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getVal(self, head):
        if head:
            index, value = self.getVal(head.next)
            return 1 + index, value + head.val * 2**index
        else:
            return 0, 0
        
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        index, val = self.getVal(head)
        return val
