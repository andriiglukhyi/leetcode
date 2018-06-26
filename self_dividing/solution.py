class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numbers = []
        for number in range(left, right+1):
            st = str(number)
            if '0' not in st:
                flag = True
                for item in st:
                    if number % int(item) != 0:
                        flag = False
                if flag:
                    numbers.append(number)
        return(numbers)
        