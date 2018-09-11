class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def foo(l, r, path):
            if  l == 0 and r == 0 :
                res.append(path[:])
                return
            if r >= l:
                if l != 0:
                    foo(l-1, r, path+'(')
                if r != 0:
                    foo(l, r-1, path+')')
        res = []
        foo(n-1, n, "(")
        print(res)
        return res

ne = Solution()
ne.generateParenthesis(10)