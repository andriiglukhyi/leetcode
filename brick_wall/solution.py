class Solution(object):
    def leastBricks(self, wall):
        mp = dict()
        for row in wall:
            count = 0
            for brick in row[:-1]: # avoid counting wall edge
                count += brick
                if count not in mp:
                    mp[count] = 1
                else:
                    mp[count] += 1
        if mp == {}:
            return len(wall)
        least = len(wall) - max(mp.values())
        return least