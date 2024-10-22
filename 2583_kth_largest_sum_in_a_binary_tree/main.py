# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []

        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if len(level_sums) < k:
                heappush(level_sums, level_sum)
            elif len(level_sums) == k and level_sum > level_sums[0]:
                heappop(level_sums)
                heappush(level_sums, level_sum)
        
        if len(level_sums) < k:
            return -1
        return level_sums[0]

        
