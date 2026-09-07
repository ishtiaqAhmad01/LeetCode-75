# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left``
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return None
        
        if root.val == key:
            return self.helper(root)

        dummy = root

        while root:
            if(root.val > key):
                # key is on left side

                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                else:
                    root = root.left
            else:
                # key is on right side
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                else:
                    root = root.right
        
        return dummy
        
    
    def helper(self, root):
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        
        rightchild = root.right
        lastright = self.findlastright(root.left)
        lastright.right = rightchild

        return root.left

    def findlastright(self, root):
        if root.right == None:
            return root
        
        return self.findlastright(root.right)


    
