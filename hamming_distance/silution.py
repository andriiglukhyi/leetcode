class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        print(bin(x), bin(y), bin(x ^ y))
        return bin(x ^ y).count("1")
example = Solution()

print(example.hammingDistance(3,4))
print(3^4)