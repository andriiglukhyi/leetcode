class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None

        if l1.val < l2.val:
            mergehead = ListNode(l1.val)
            mergehead.next = self.mergeTwoLists(l1.next, l2)
        else:
            mergehead = ListNode(l2.val)
            mergehead.next = self.mergeTwoLists(l1, l2.next)
            
        return mergehead