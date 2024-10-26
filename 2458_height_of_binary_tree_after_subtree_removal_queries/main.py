# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        answers = {}
        heights = {None: 0}

        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            height = max(left, right) + 1
            heights[node] = height
            return height
        
        dfs(root)
        
        def replace_high_nodes(high_nodes, node):
            high_nodes.append(node)
            high_nodes.sort(key=lambda x: heights[x], reverse=True)
            high_nodes.pop()
        
        # Do a bfs
        queue = deque([root])
        depth = 0
        while queue:
            level_size = len(queue)

            # Find the highest and second highest node
            high_nodes = [None, None]

            for node in queue:
                replace_high_nodes(high_nodes, node)
            
            for node in queue:
                if node == high_nodes[0]:
                    answers[node.val] = heights[high_nodes[1]] + depth
                else:
                    answers[node.val] = heights[high_nodes[0]] + depth

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        result = []
        for query in queries:
            result.append(answers[query] - 1)
        
        return result

        """
        val_to_node = {}
        heights = {None: 0}
        parents = {}

        def dfs(node, parent):
            if node is None:
                return 0
            
            val_to_node[node.val] = node
            parents[node] = parent
            
            height_left = dfs(node.left, node)
            height_right = dfs(node.right, node)

            heights[node] = max(height_left, height_right) + 1
            return heights[node]
        
        dfs(root, None)
        result = []

        for query in queries:
            node = val_to_node[query]
            curr_depth = 0

            while node:
                parent = parents[node]
                if parent is None:
                    result.append(curr_depth - 1)
                    break
                other = parent.left if node == parent.right else parent.right

                curr_depth = max(curr_depth, heights[other]) + 1
                node = parent
        
        return result
        """

