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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        result = 0
        stack = [(root, root.val)]

        while stack:
            node, val = stack.pop()

            if node.left is None and node.right is None:
                result += val
                continue
            
            if node.left:
                stack.append((node.left, val * 10 + node.left.val))
            if node.right:
                stack.append((node.right, val * 10 + node.right.val))
        
        return result


