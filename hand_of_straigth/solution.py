class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if W == 1:
            return True
        if len(hand) % W:
            return False
        cnt = collections.Counter(hand)
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
                