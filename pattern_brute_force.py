def brute_force(s, p):
    # introduce cinvention betwen notation
    n,m = len(s), len(p)
    #try every  potential starting index within T 
    for i in range(n-m+1):
        k = 0
        while k < m and s[i+k] == p[k]:
            k += 1
        if k == m:
            return i
    return -1

print(brute_force('fdhgfhsdhjshkdfhksdfkjsdkjfskjfhkjsd', 'gfhsdhjsh'))