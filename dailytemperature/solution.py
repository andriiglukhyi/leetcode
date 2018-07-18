class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        end = []
        if not temperatures:
            return False
        # go from 0 to  len temp -1 becouse range is exclusive
        for number in range(len(temperatures)):
            j = number
            while temperatures[number] >=  temperatures[j]:
                if j < len(temperatures)-1:
                    j += 1
                else:
                    end.append(0)
                    break
            end.append(j - number)
        return end