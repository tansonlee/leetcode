# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ordered_nodes = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            ordered_nodes.append(node.val)
            dfs(node.right)
        
        dfs(root)
        print(ordered_nodes)
        
        def insert_helper(node, val):
            if node is None:
                return TreeNode(val)
            if node.val < val:
                node.right = insert_helper(node.right, val)
            if node.val > val:
                node.left = insert_helper(node.left, val)
            return node

        def insert(nodes, node):
            if len(nodes) == 0:
                return None

            mid = nodes[len(nodes) // 2]

            node = insert_helper(node, mid)

            node.left = insert(nodes[:len(nodes) // 2], node.left)
            node.right = insert(nodes[len(nodes) // 2 + 1:], node.right)
            return node
        
        return insert(ordered_nodes, None)

