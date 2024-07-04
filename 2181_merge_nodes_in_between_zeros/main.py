# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr_result_ptr = result

        curr = head.next
        while curr:
            s =  0
            while curr and curr.val != 0:
                s += curr.val
                curr = curr.next
            
            curr_result_ptr.next = ListNode(s)
            curr_result_ptr = curr_result_ptr.next

            curr = curr.next
        
        return result.next




        
