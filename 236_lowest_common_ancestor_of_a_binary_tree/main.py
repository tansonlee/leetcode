# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_path(node, target, path):
            if node is None:
                return None

            if node == target:
                return path + [node]
            
            # look left
            left_res = get_path(node.left, target, path + [node])
            if left_res is not None:
                return left_res

            # look right
            right_res = get_path(node.right, target, path + [node])
            if right_res is not None:
                return right_res 
            
            return None
        
        p_path = get_path(root, p, [])
        q_path = get_path(root, q, [])

        p_path_set = set([x.val for x in p_path])
        for node in reversed(q_path):
            if node.val in p_path_set:
                return node
        
        return None


            

        
