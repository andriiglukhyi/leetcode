# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        end = []
        level = Queue()
        next_level = Queue()
        end.append([root.val])
        if root.left:
            end.append([root.left.val])
            level.put(root.left)
        if root.right:
            level.put(root.right)
        def _swap(level, next_level):
            cur = level.get()
            lefts = []
            while cur:
                if cur.left:
                    lefts.append(cur.val)
                    next_level.put(cur.left)
                if cur.right:
                    next_level.put(cur.right)
                cur = level.get()
                print(cur.val)
            if len(lefts) > 0:
                end.append(lefts)
            print(dir(level))
            level, next_level = next_level, level
        while not level.empty():
            _swap(level, next_level)
        print(end)