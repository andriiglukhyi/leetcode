def circularArrayLoop(self, nums):
    n = len(nums)

    for i, num in enumerate(nums):

        pos = num > 0               # direction of movements
        j = (i + num) % n           # take the first step
        steps = 1

        while steps < n and nums[j] % n != 0 and (nums[j] > 0) == pos:
            j = (j + nums[j]) % n   # take the next step
            steps += 1

        if steps == n:              # loop is found
            return True

        nums[i] = 0
        j = (i + num) % n           # set everything visited to zero to avoid repeating
        while nums[j] % n != 0 and (nums[j] > 0) == pos:
            j, nums[j] = (j + nums[j]) % n, 0

    return False