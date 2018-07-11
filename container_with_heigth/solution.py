class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # set mx size
        mx = height[0]*height[0]
        end = [0,0]
        for number in range(len(height)):
            i = j = number
            print(i, j, number)
            print(height[i], height[j])
            counter = 0
            while i >= 0 or j <= len(height)-1:
                if i >= 0:
                    if height[i]>= height[number]:
                        counter += 1
                if j <= len(height)-1:
                    if height[j]>= height[number]:
                        counter += 1
                i += 1
                j += 1
            if (counter + 1)*height[number] > mx:
                mx = (counter + 1)*height[number]
                end = [i, j]
        return mx
