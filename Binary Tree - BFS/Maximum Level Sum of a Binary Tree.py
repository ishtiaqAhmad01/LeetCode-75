# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        q = deque([root])
        ans = {}
        level = 1

        while q:
            level_size = len(q)
            curr_level_sum = 0

            for _ in range(level_size):
                curr = q.popleft()

                curr_level_sum += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            ans[level] = curr_level_sum
            level+=1
            
        return max(ans, key=ans.get)
            




