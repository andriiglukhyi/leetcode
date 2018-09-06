# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visited = set()
        copy = set()
        def walk(node):
            if node is None:
                return
            if node.val in visited:
                copy.add(node.val)
            else:
                visited.add(node.val)
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
        if not root:
            return False
        walk(root)
        if len(visited) == 1:
            return list(visited)
        return list(copy)