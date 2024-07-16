# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Returns (<start value depth>, <dest value path>)
        def helper(node, curr_path):
            if node is None:
                return (None, None)

            start_val_depth = None
            end_val_path = None

            if node.val == startValue:
                start_val_depth = 0
            if node.val == destValue:
                end_val_path = ""
            
            l_start_val_depth, l_dest_val_path = helper(node.left, curr_path)
            r_start_val_depth, r_dest_val_path = helper(node.right, curr_path)

            if l_start_val_depth is not None and l_dest_val_path is not None:
                return (l_start_val_depth, l_dest_val_path)
            if r_start_val_depth is not None and r_dest_val_path is not None:
                return (r_start_val_depth, r_dest_val_path)

            if l_start_val_depth is not None:
                start_val_depth = l_start_val_depth + 1
            if r_start_val_depth is not None:
                start_val_depth = r_start_val_depth + 1
            
            if l_dest_val_path is not None:
                end_val_path = l_dest_val_path + "L"
            if r_dest_val_path is not None:
                end_val_path = r_dest_val_path + "R"

            return (start_val_depth, end_val_path)
        
        depth, path = helper(root, "")
        return 'U' * depth + path[::-1]

            

        # # Find path from root to start and destination.
        # def find_path(node, target, curr_path):
        #     if node is None:
        #         return None
        #     if node.val == target:
        #         return curr_path + [node]
        #     find_left = find_path(node.left, target, curr_path + [node])
        #     if find_left:
        #         return find_left
        #     return find_path(node.right, target, curr_path + [node])
        
        # start_path = find_path(root, startValue, [])
        # end_path = find_path(root, destValue, [])

        # # Determine the lowest common ancestor.
        # start_path_set = set(start_path)
        # LCA = None
        # for node in reversed(end_path):
        #     if node in start_path_set:
        #         LCA = node
        #         break

        # # Create the path.
        # start_index = None
        # end_index = None
        # for i in range(len(start_path)):
        #     if start_path[i].val == LCA.val:
        #         start_index = i
        #         break
        # for i in range(len(end_path)):
        #     if end_path[i].val == LCA.val:
        #         end_index = i
        #         break
        
        # # Determine paths from start to LCA and LCA to end
        # start_to_LCA = 'U' * (len(start_path) - start_index - 1)
        # end_to_LCA = ''
        # for i in range(end_index, len(end_path)):
        #     if end_path[i].val == destValue:
        #         break
        #     if end_path[i].left == end_path[i + 1]:
        #         end_to_LCA += 'L'
        #     else:
        #         end_to_LCA += 'R'
        
        # return start_to_LCA + end_to_LCA

