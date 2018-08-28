class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for item in tokens:
            try:
                int(item)
                stack.append(int(item))
            except ValueError:
                item1 = stack.pop()
                item2 = stack.pop()
                if item == "*":
                    if item1 == 0 or item2 == 0:
                        item3 = 0
                    item3 = item1*item2
                elif item == "/":
                    if item1 == 0 or item2 == 0:
                        item3 = 0
                    item3 = int(float(item2)/item1)
                elif item == "+":
                    item3 = item1+item2
                elif item == "-":
                    item3 = item2-item1
                stack.append(item3)
        return stack[0]

# faster solution

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operand = {
            '*': True
            '/': True
            '+': True
            '-': True
        }
        stack = []
        for item in tokens:
            if item in operand:
                item1 = stack.pop()
                item2 = stack.pop()
                if item == "*":
                    if item1 == 0 or item2 == 0:
                        item3 = 0
                    item3 = item1*item2
                elif item == "/":
                    if item1 == 0 or item2 == 0:
                        item3 = 0
                    item3 = int(float(item2)/item1)
                elif item == "+":
                    item3 = item1+item2
                elif item == "-":
                    item3 = item2-item1
                stack.append(item3)
            else:
                stack.append(int(item))
        return stack[0]