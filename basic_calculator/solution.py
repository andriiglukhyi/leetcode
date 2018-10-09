class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def multiply(a, b, sign):
            while not s[a].isnumeric():
                a -= 1
            while not s[b].isnumeric():
                b += 1
            if s[sign] == "*":
                ans = int(s[a])*int(s[b])
            elif a[sign] == "/":
                ans = int(s[a]) // int(s[b])
            return s[:a]+str(ans)+s[b+1:]
        for item in reversed(range(len(s)-1)):
            if s[item] == ("*" or "/"):
                s = multiply(item-1, item+1, item)
        def ad(s):
            qu = []
            for item in s:
                if len(qu) == 3:
                    if qu[1] == "+":
                        ans = int(qu[0]) + int(qu[2])
                        qu = [ans]
                    elif qu[1] == "-":
                        ans = int(qu[0]) - int(qu[2])
                        qu = [ans]
                    else:
                        qu = []
                    
                if item.isnumeric() or item == "+" or item == "-":
                    qu.append(item)
            if len(qu) == 3:
                    if qu[1] == "+":
                        ans = int(qu[0]) + int(qu[2])
                        qu = [ans]
                    elif qu[1] == "-":
                        ans = int(qu[0]) - int(qu[2])
                        qu = [ans]
                    else:
                        qu = []
            if qu:
                return qu[0]
            return int(s)
        return ad(s)
        