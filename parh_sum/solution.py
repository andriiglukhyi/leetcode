# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.dfs(root, sum, [])
        return self.res
        
    def dfs(self, root, sum, tmp):
        sum -= root.val
        tmp.append(root.val)
        if sum == 0:
            if not root.left and not root.right:
                self.res.append(tmp[:])
        else:
            if root.left:
                self.dfs(root.left, sum, tmp)
            if root.right:
                self.dfs(root.right, sum, tmp)
        tmp.pop()