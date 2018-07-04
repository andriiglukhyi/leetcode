def countPrimes(n):  
    if n <= 2:
        return 0
    res = [True] * n
    res[0] = res[1] = False
    for i in range(2, int(n**0.5)+1):
        if res[i] == True:
            for j in range(i, (n-1)//i+1):
                res[i*j] = False
    return sum(res)


    