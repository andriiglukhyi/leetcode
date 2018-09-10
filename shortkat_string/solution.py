a = 'aaaabbbbbcccccdddd'
i = -1
j = i
while i > -len(a)-1 or j > -(len(a)-1):
    print(a[i], a[j], len(a))
    while a [i] == a[j] and j > -(len(a)-1):
        j -=1
    a = a[:j]+str(i-j)+a[i:]
    i -= 2
    j = i