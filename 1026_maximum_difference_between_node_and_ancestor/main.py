# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, maxi, mini):
            if node is None:
                return abs(maxi - mini)
            
            new_max = max(maxi, node.val)
            new_min = min(mini, node.val)
            return max(helper(node.left, new_max, new_min), helper(node.right, new_max, new_min))
        
        return helper(root, root.val, root.val)
        
