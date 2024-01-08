# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Possible to further optimize by not looking down subtrees
that we already know will not be in the range.
"""

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        result = 0
        if root.val >= low and root.val <= high:
            result += root.val
        result += self.rangeSumBST(root.left, low, high)
        result += self.rangeSumBST(root.right, low, high)

        return result 
