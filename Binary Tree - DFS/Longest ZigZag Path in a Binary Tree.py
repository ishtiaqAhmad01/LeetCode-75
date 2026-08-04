# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.current_max = 0
        def traverse_zigzag(node, direction, current_length):
            self.current_max = max(current_length, self.current_max)

            if not node:
                return
            if direction == "left":
                traverse_zigzag(node.right, "right", current_length+1)
                traverse_zigzag(node.left, "left", 0)
            else:
                traverse_zigzag(node.left, "left", current_length+1)
                traverse_zigzag(node.right, "right", 0)
            
        
        traverse_zigzag(root.left, "left", 0)
        traverse_zigzag(root.right, "right", 0)
        
        return self.current_max



            
        
        
