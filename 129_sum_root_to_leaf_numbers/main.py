# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, acc):
            if node is None:
                return 0
            
            curr = acc * 10 + node.val
            if node.left is None and node.right is None:
                return curr
            
            return helper(node.left, curr) + helper(node.right, curr)
        
        return helper(root, 0)

