# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(node, additional):
            if node is None:
                return 0
            
            right_sum = helper(node.right, additional)
            left_sum = helper(node.left, additional + node.val + right_sum)
            total_sum = left_sum + right_sum + node.val

            node.val += right_sum + additional
            return total_sum
        
        helper(root, 0)
        return root

        
