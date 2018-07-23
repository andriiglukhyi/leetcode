class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == "":
            return True
        st = A
        for _ in range(len(A)):
            st = st[1:]+st[0]
            if st == B:
                return True
        return False
        