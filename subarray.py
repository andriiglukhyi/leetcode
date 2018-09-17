def max_sub_array_sum(a):
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1, len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
         
    print(max_so_far)

max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3])