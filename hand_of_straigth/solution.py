class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)<W or len(hand) == 0:
            return False
        hand = sorted(set(hand))
        groups = []
        for item in range(len(hand)):
            j = item
            flag = True
            counter = 1
            if j+W > len(hand):
                break
            while counter < W and flag:
                if hand[j]==hand[j+1] -1:
                    print(hand[j])
                    j += 1 
                    counter += 1
                else:
                    flag = False
            if flag:
                groups.append(hand[item:j+1])
        print(len(groups), W)
        if len(groups) >= W:
            return True
        return False
                