# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # determine the parent node for each node
        parents = {}
        # also find the start node
        start_node = None
        s = [root]
        while len(s) > 0:
            curr = s.pop()
            if curr.left is not None:
                parents[curr.left] = curr
                s.append(curr.left)
            if curr.right is not None:
                parents[curr.right] = curr
                s.append(curr.right)
            
            if curr.val == start:
                start_node = curr
        
        # dfs from the start node to find the furthest node
        max_depth = 0
        s = [(start_node, 0)]
        visited = set()
        while len(s) > 0:
            curr, d = s.pop()
            if curr in visited:
                continue
            visited.add(curr)
            max_depth = max(max_depth, d)
            if curr.left is not None:
                s.append((curr.left, d + 1))
            if curr.right is not None:
                s.append((curr.right, d + 1))
            if curr in parents:
                s.append((parents[curr], d + 1))
        
        return max_depth
            




        


        
