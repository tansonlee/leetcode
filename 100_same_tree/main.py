# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #####
        # Recursive
        #####
        def helper(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            return helper(a.left, b.left) and helper(a.right, b.right)
        return helper(p, q)

        #####
        # Iterative
        #####
        stack = [p, q]
        while len(stack) > 0:
            a = stack.pop()
            b = stack.pop()

            if a is None and b is None:
                continue
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            
            stack.append(a.left)
            stack.append(b.left)

            stack.append(a.right)
            stack.append(b.right)
        return True

        
