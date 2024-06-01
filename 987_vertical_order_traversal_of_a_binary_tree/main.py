# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_by_col = defaultdict(list)

        def helper(node, row, col):
            if node is None:
                return

            nodes_by_col[col].append((node.val, row))
            helper(node.left, row + 1, col - 1)
            helper(node.right, row + 1, col + 1)
        helper(root, 0, 0)
        
        nodes_by_col_list = [(col, nodes_by_col[col]) for col in nodes_by_col]
        nodes_by_col_list.sort()


        nodes_by_col_list = [x[1] for x in nodes_by_col_list]

        def compare(p1, p2):
            if p1[1] > p2[1]:
                return 1
            if p1[1] < p2[1]:
                return -1
            if p1[0] > p2[0]:
                return 1
            if p1[0] < p2[0]:
                return -1
            return 0
        
        for l in nodes_by_col_list:
            l.sort(key=cmp_to_key(compare))
        
        for i in range(len(nodes_by_col_list)):
            nodes_by_col_list[i] = [x[0] for x in nodes_by_col_list[i]]
        
        return nodes_by_col_list

