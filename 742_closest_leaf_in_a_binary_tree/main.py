# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        k_node = None
        parent = {}

        # First bfs to determine each nodes parent and find the k_node
        queue = deque([(root, None)])
        while queue:
            node, p = queue.popleft()

            if node.val == k:
                k_node = node
            
            parent[node.val] = p

            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        
        # Second bfs starting from k_node to find the nearest leaf
        queue = deque([k_node])
        seen = set()
        while queue:
            node = queue.popleft()
            if node.val in seen:
                continue
            seen.add(node.val)

            # Found a leaf
            if node.left is None and node.right is None:
                return node.val
            
            neighbors = [node.left, node.right, parent[node.val]]
            for neighbor in neighbors:
                if neighbor is not None:
                    queue.append(neighbor)
        
        # Did not find a leaf (impossible)
        return 0





        
