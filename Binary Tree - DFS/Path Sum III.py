# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.ans = 0

        def path(node, current_sum):
            current_sum += node.val

            if node and not node.right and not node.left:
                if current_sum == targetSum:
                    self.ans+=1
                return 0

            if current_sum == targetSum:
                    self.ans+=1

            if node.left:
                path(node.left, current_sum)
            if node.right:
                path(node.right, current_sum)
        
        def traverse(node):
            if not node:
                return
            
            path(node, 0)

            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        
        return self.ans


            



        
