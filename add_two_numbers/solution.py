# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        st1 = ''
        st2 = ''
        while l1:
            st1 += str(l1.val)
            l1 = l1.next
        while l2:
            st2 += str(l2.val)
            l2 = l2.next
        end = list(str(int(st1[::-1]) + int(st2[::-1])))[::-1]
                   
        for item in range(len(end)):
            end[item] = int(end[item])
        return end