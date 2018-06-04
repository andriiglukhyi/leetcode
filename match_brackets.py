def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    opn = ['(', '{', '[']
    closed = [')',  '}', ']']
    if s == "":
        return True
    if len(s) == 1:
        return False
    a = []
    import pdb; pdb.set_trace()
    for item in s:
        print(s, item)
        if item in opn:
            a.append(item)
        if item in closed:
            if a == []:
                return False
            if opn.index(a[-1]) == closed.index(item):
                a.pop()
    return 


isValid('()')