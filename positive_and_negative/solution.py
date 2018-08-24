def move(arr):
    # Count negative numbers
    n = len(arr)
    count_negative = 0
    for i in range(n): 
        if (arr[i] < 0):
            count_negative += 1
    i = 0
    j = i + 1
    while i != count_negative:
        if arr[i] < 0:
            i +=1
            j = i + 1
        elif arr[i] > 0 and j < n:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            j += 1
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6 ]
print(arr)
move(arr)
print(arr)
