# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #####
        # each node approach
        #####
        def helper(node): # returns (depth, ans)
            if node is None:
                return 0, 0
            left_depth, left_ans = helper(node.left)
            right_depth, right_ans = helper(node.right)
            curr_ans = left_depth + right_depth + 1
            curr_depth = max(left_depth, right_depth) + 1

            return curr_depth, max(curr_ans, left_ans, right_ans)
        
        _, result = helper(root)
        
        return result - 1

        #####
        # double dfs approach
        #####
        # find the deepest node
        def deepest(node):
            if node is None:
                return None, 0
            if node.left is None and node.right is None:
                return node, 1
            left, left_depth = deepest(node.left)
            right, right_depth = deepest(node.right)
            if left_depth > right_depth:
                return left, left_depth + 1
            else:
                return right, right_depth + 1
        
        deepest_node, _ = deepest(root)

        # find the parents for each node
        parents = {}
        parents[root] = None
        def get_parents(node):
            if node is None:
                return
            if node.left is not None:
                parents[node.left] = node
                get_parents(node.left)
            if node.right is not None:
                parents[node.right] = node
                get_parents(node.right)
        get_parents(root)

        # from the deepest node, find the farthest away node
        visited = set()
        def farthest(node):
            if node is None:
                return 0
            visited.add(node)

            neighbors = [node.left, node.right, parents[node]]
            result = 0
            for n in neighbors:
                if n is not None and n not in visited:
                    result = max(result, 1 + farthest(n))
            
            return result
        
        return farthest(deepest_node)

