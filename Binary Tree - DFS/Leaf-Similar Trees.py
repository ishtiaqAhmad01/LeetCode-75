# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        def extrect_leaf(node, arr):
            if node is None:
                return
            
            if node.left == None and node.right == None:
                arr.append(node.val)
            
            extrect_leaf(node.left, arr)
            extrect_leaf(node.right, arr)
        
        arr1  = []
        arr2 = []

        extrect_leaf(root1, arr1)
        extrect_leaf(root2, arr2)

        return arr1 == arr2


            

        
