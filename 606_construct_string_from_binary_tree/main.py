# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        result = str(root.val)
        left = self.tree2str(root.left)
        if left != "":
            right = self.tree2str(root.right)
            result += f"({left})"
            if right != "":
                result += f"({right})"
        else:
            right = self.tree2str(root.right)
            if right!= "":
                result += f"()({right})"
        return result
        
