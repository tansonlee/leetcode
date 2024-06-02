# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if node is None:
                return
            
            if depth >= len(result):
                result.append(0)
            result[depth] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return result




        if root is None:
            return []
        queue = deque([root])
        result = []

        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if i == l - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result




