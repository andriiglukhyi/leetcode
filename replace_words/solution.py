class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        d = {}
        for item in dict:
            d[item] = 0
        nw = sentence.split(" ")
        for word in range(len(nw)):
            for letter in range(len(nw[word])):
                if nw[word][:letter] in d:
                    nw[word] = nw[word][:letter]
        return(" ".join(nw))