"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        nodes = []

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        
        dfs(root)
        
        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]
            nodes[i + 1].left = nodes[i]
        
        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]

        return nodes[0]
        
            
        
