# Dynamic Programming implementation of longest bitonic subsequence problem
"""
lbs() returns the length of the Longest Bitonic Subsequence in
arr[] of size n. The function mainly creates two temporary arrays
lis[] and lds[] and returns the maximum lis[i] + lds[i] - 1.
 
lis[i] ==> Longest Increasing subsequence ending with arr[i]
lds[i] ==> Longest decreasing subsequence starting with arr[i]
"""
 
def lbs(arr):
    n = len(arr)
 
 
    # allocate memory for LIS[] and initialize LIS values as 1
    # for minus
    lis = [0 for i in range(n-2)]
 
    # Compute LIS values from left to right
    for i in range(0 , n-2):
        if arr[i] > arr[i+1]:
            lis[i] = 1
        else:
            lis[i] = -1
 
    # allocate memory for LDS and initialize LDS values for
    # all indexes
    ans = []
     
    # Compute LDS values from right to left
    counter = 0
    for i in range(len(lis)):
        if arr[i] == arr[i+1]:
            counter += 1
        else:
            ans.append(counter + 1)
     
    biggest = 0
    # Return the maximum value of (lis[i] + lds[i] - 1)
    for i in range(len(ans)-1):
        if ans[i] + ans[i+1] > biggest:
            biggest = ans[i] + ans[i+1]
     
    return biggest
# Driver program to test the above function
arr =  [1,2,3,4,5,4,3,4,5,6,7,2,1,0]
print(lbs(arr))