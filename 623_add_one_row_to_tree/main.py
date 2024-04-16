# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        if root is None:
            return None

        if depth == 2:
            new_left = TreeNode(val, root.left, None)
            new_right = TreeNode(val, None, root.right)
            return TreeNode(root.val, new_left, new_right)
        
        new_left = self.addOneRow(root.left, val, depth - 1)
        new_right = self.addOneRow(root.right, val, depth - 1)
        return TreeNode(root.val, new_left, new_right)

