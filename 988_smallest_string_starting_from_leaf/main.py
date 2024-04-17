# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = None

        def helper(node, path):
            if node is None:
                return

            curr = chr(97 + node.val) + path
            if node.left is None and node.right is None:
                if self.res is None or curr < self.res:
                    self.res = curr
                    return
            
            helper(node.left, curr)
            helper(node.right, curr)
        
        helper(root, "")
        return self.res

