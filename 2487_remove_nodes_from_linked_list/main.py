# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        back = reverse(head)
        curr_max = back.val
        curr = back
        while curr:
            nxt = curr.next
            while nxt and nxt.val < curr_max:
                nxt = nxt.next
            curr.next = nxt
            if nxt:
                curr = nxt
                curr_max = curr.val
            else:
                break

        front = reverse(back)
        return front

                

        
