# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def is_pseudo_palindromic(counts):
            odd_counts = 0
            for num in counts:
                if counts[num] % 2 == 1:
                    odd_counts += 1
                    if odd_counts >= 2:
                        return False
            return True

        def dfs(node, path):
            path[node.val] += 1

            result = 0
            if node.left is None and node.right is None:
                if is_pseudo_palindromic(path):
                    result = 1
            else:
                if node.left is not None:
                    result += dfs(node.left, path)
                if node.right is not None:
                    result += dfs(node.right, path)

            path[node.val] -= 1
            return result 
        
        return dfs(root, defaultdict(int))
