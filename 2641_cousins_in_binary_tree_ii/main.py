# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        children_sums = {None: root.val}

        def get_children_sums(node):
            if node is None:
                return
            s = 0
            if node.left:
                s += node.left.val
            if node.right:
                s += node.right.val
            
            children_sums[node] = s

            get_children_sums(node.left)
            get_children_sums(node.right)
        
        get_children_sums(root)

        queue = deque([(root, None)])

        while queue:
            level_size = len(queue)

            # Compute the cousin sums.
            total_sum = 0
            for node, _ in queue:
                total_sum += node.val
            
            for node, parent in queue:
                val = total_sum - children_sums[parent]
                node.val = val

            for _ in range(level_size):
                node, _ = queue.popleft()
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
        
        return root

        
