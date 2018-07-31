# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        len = 0
        while cur:
            len += 1
            cur = cur.next
        if len % 2 == 0:
            midle = len/2 + 1
        else:
            midle = len // 2 + len % 2
        cur = head
        while midle > 1:
            cur = cur.next
            midle -= 1
        return cur
        