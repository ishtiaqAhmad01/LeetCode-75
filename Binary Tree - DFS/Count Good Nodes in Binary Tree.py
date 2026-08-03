# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def good_nodes(node, curr_max):
            if not node:
                return 0

            if node.val >= curr_max:

                return 1 + good_nodes(node.left, node.val) + good_nodes(node.right, node.val)
            else:
                return good_nodes(node.left, curr_max) + good_nodes(node.right, curr_max)
        
        return good_nodes(root, root.val)
