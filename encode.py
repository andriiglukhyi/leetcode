# Given the alphabet encoded as numbers (e.g., a=1, b=2, ..., z=26), and a sequence of numbers (e.g., "23413259802"), 
# how many strings can be generated.  

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # corner cases: first is leetcode-specific, second is to deal with invalid inputs.
        if not s:
            return 0
        elif s[0] == "0":
            return 0

        # num_decodings[i] corresponds to the number of ways to decode s[i:]
        num_decodings = [0] * (len(s)+1)

        # initialize base cases
        num_decodings[len(s)] = 1
        num_decodings[len(s)-1] = 1 if s[-1] != "0" else 0

        # iterate over the input, backwards
        for i in reversed(range(len(s)-1)):

            # 0 has no mapping to a letter, so we skip it.
            if s[i] == "0": continue

            num_decodings[i] = num_decodings[i+1]
            if int(s[i:i+2]) <= 26:
                num_decodings[i] += num_decodings[i+2]

        return num_decodings[0]


if __name__ == "__main__":
    for i in ["12", "0", "10", "103", "1032", "23413259802"]:
        print(Solution().numDecodings(i))