# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = root 
        queue = deque([root])
        while len(queue) > 0:
            num_nodes_at_level = len(queue)
            for _ in range(num_nodes_at_level):
                curr = queue.popleft()
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            
            if len(queue) > 0:
                result = queue[0]
        
        return result.val

