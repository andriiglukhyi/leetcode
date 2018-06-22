class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if W == 1 and len(hand) > 0:
            return True
        if len(hand) % W:
            return False
        cnt = {}
        for item in hand:
            try:
                cnt[item] += 1
            except KeyError:
                cnt[item] = 1
        while cnt:
            start = min(cnt)
            cnt[start] -= 1
            if cnt[start] == 0:
                del cnt[start]
            for i in range(1, W):
                if start + i not in cnt:
                    return False
                cnt[start+i] -= 1
                if cnt[start+i] == 0:
                    del cnt[start+i]
        return True