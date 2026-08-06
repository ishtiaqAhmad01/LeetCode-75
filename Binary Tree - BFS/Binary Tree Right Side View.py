# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            current_right = None
            level_size = len(q)

            for _ in range(level_size):
                curr = q.popleft()
                current_level = curr.val

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            ans.append(current_level)
        
        return ans
                
            
            



        

        
