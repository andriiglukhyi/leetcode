# Function which pushes all
# zeros to end of an array.
def pushZerosToEnd(arr, n):
    count = 0 # Count of non-zero elements
     
    # Traverse the array. If element 
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        if arr[i] != 0:             
            # here count is incremented
            arr[count] = arr[i]
            print(arr)

            count+=1
     
    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all 
    # elements 0 from count to end.
    while count < n:
        print(arr)
        arr[count] = 0
        count += 1
    print(arr)

pushZerosToEnd([0,1,2,3,4,0,3,4], 8)