# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        run_length = -1

        curr_num = -1
        curr_run_length = -1
        def inorder(node):
            nonlocal modes, run_length, curr_num, curr_run_length
            if node is None:
                return
            
            inorder(node.left)
            if len(modes) == 0:
                modes = [node.val]
                run_length = 1
                curr_num = node.val
                curr_run_length = 1
            else:
                if node.val == curr_num:
                    curr_run_length += 1
                else:
                    curr_num = node.val
                    curr_run_length = 1
                
                if curr_run_length == run_length:
                    modes.append(node.val)
                if curr_run_length > run_length:
                    modes = [node.val]
                    run_length = curr_run_length

            inorder(node.right)
        


        inorder(root)
        return modes



        if root is None:
            return []

        counts = {}

        def helper(node, counts):
            if node is None:
                return
            if node.val not in counts:
                counts[node.val] = 0
            counts[node.val] += 1
            helper(node.left, counts)
            helper(node.right, counts)
        
        helper(root, counts)

        modes = []
        for num in counts:
            if len(modes) == 0:
                modes = [num]
                continue
            
            if counts[num] == counts[modes[0]]:
                modes.append(num)
            elif counts[num] > counts[modes[0]]:
                modes = [num]
        
        return modes

        
