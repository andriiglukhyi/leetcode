class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        r = []
        l=len(S)
        for x in range(l):
            a, b =S[x-l::-1].find(C), S[x:].find(C)
            if(a < 0 or (a >= b and b >0)): r.append(b)
            else : r.append(a)
        return r
        