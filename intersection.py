a = [2, 3, 3, 4, 6, 6, 8]
b = [3, 10, 6, 7, 9]

def intersection(a, b):
    for item in range(len(b)):
        if b[item] not in a:
            b[item] = 0
    while 0 in b:
        b.remove(0)
    print(b)

intersection(a,b)