# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def find_depth(node):
            if not node:
                return 0
        
            return max(1+find_depth(node.left), 1+find_depth(node.right))
        
        return find_depth(root)
