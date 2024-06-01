"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        old_to_new = {}

        def dfs_create(node, visited):
            if node in visited:
                return
            old_to_new[node] = Node(node.val)
            visited.add(node)
            for neighbor in node.neighbors:
                dfs_create(neighbor, visited)
        dfs_create(node, set())

        for old in old_to_new:
            for neighbor in old.neighbors:
                old_to_new[old].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]
        
