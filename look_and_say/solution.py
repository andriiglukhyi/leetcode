def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    s = str(1)
    while n > 0:
        temp = ''
        j = i = 0
        counter = 0
        while j < len(s):
            if s[i] != s[j]:
                temp += str(counter)+s[i]
                i = j
            else:
                j += 1
                counter += 1
            if i != j:
                temp += str(counter) + s[i]
            
        s = temp
        n -= 1
countAndSay(5)