def find_even_index(arr):
    for N in arr:
        if sum(arr[0:N]) == sum(arr[N:len(arr)]):
            return N