# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_to_nodes = defaultdict(list)

        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            if node is None:
                continue

            col_to_nodes[col].append(node.val)
            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))
        
        nodes = [(col, col_to_nodes[col]) for col in col_to_nodes]
        nodes.sort()
        return [x[1] for x in nodes]

        col_to_nodes = defaultdict(list)
        counter = 0

        def helper(node, row, col):
            nonlocal counter
            if node is None:
                return
            col_to_nodes[col].append((row, counter, node.val))
            counter += 1
            helper(node.left, col - 1, row + 1)
            helper(node.right, col + 1, row + 1)
        
        helper(root, 0, 0)
        
        col_and_nodes = [(col, col_to_nodes[col]) for col in col_to_nodes]
        col_and_nodes.sort()
        col_and_nodes = [x[1] for x in col_and_nodes]
        for i in range(len(col_and_nodes)):
            col_and_nodes[i].sort()
            col_and_nodes[i] = [x[2] for x in col_and_nodes]
        
        return col_and_nodes

