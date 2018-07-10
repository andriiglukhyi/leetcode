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
            a, b = S[x-l::-1].find(C), S[x:].find(C)
            if(a < 0 or (a >= b and b >0)):
                r.append(b)
            else:
                r.append(a)
        return r

# from Dave
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        S = list(S)

        # Find indices that contain value C
        indices = []
        for i, char in enumerate(S):
            if char == C:
                indices.append(i)
                S[i] = 0

        # Left-most indices
        i = 0
        while True:
            if S[i] == 0:
                break
            S[i] = i + 1
            i += 1
        S[:i] = reversed(S[:i])

        # Right-most indices
        i = len(S) - 1
        while True:
            if S[i] == 0:
                break
            S[i] = len(S) - i
            i -= 1
        S[i + 1:] = reversed(S[i + 1:])

        # If one C, we're done
        if len(indices) == 1:
            return S

        # Handle C's by pairs
        for i in range(len(indices) - 1):
            l = indices[i]
            r = indices[i + 1]
            d = 0
            while True:
                S[l] = d
                S[r] = d
                if l >= r - 1:
                    break
                l += 1
                r -= 1
                d += 1

        return S