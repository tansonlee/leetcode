# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Path starting from root
    def path_from(self, head, root):
        if head is None:
            return True
        
        if root is None:
            return False
        
        if head.val != root.val:
            return False
        
        return self.path_from(head.next, root.left) or self.path_from(head.next, root.right)
        
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None:
            return True
        
        if root is None:
            return False
        
        if head.val == root.val:
            answer = self.path_from(head, root)
            if answer:
                return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


