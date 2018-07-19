def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums)<3:
        if len(nums) == 0:
            return []
        return max(nums)
    end = []
    counter = 0
    temp = nums[0:k]
    first = max(temp)
    temp.remove(first)
    second = max(temp)
    temp.remove(second)
    third = max(temp)
    for item in range(len(nums)-k+1):
        end.append(max(first, second, third))
        if item+k < len(nums):
            n = nums[item + k]
        else:
            n = nums[len(nums)-1]
        if n > first:
            first = n
            second = first
            third = second
            counter = 0
        elif n > second:
            second = n
            third = second
        elif n > third:
            third = n
        if counter < k:
            counter += 1
        else:
            temp = nums[item:item+k]
            first = max(temp)
            temp.remove(first)
            second = max(temp)
            temp.remove(second)
            third = max(temp)
    print(end)
            

maxSlidingWindow([-301,7825,3986,6586,4837,9414,8005,803,5827,-93,7789,2217,4263,3382,2158,7877,2394,4410,6209,8417,3574,6454,8355,3736,8425,-599,1182,-174,7669,2836,5340,1427,690,5097,9582,4565,4160,6176,1922,235,9070,8117,9027,5705,-586,5584,9256,3162,8454,5514,9313,4566,1281,9196,2270,7889,1190,-76,-551,4360,85,9031,568,8318,228,9555,890,9465,8058,1041,7710,-746,567,6490,8774,7507,7389,6195,309,1644,7350,4054,348], 5)