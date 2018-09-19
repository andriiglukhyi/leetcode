class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        end = []
        j = i = 0
        while j < len(S):
            if S[i] == S[j]:
                j += 1 
            else:
                if j - i >= 3:
                    end.append([i, j-1])
                i = j
                j += 1
        if j - i >= 3:
            end.append([i, j-1])
        return end
                    