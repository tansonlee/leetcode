# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        def helper(node):
            if node is None:
                return None
            if node.val in nums:
                return helper(node.next)
            
            node.next = helper(node.next)
            return node
        
        return helper(head)
        

        
