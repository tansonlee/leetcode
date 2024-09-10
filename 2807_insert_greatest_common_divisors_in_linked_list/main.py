# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Euclidian algorithm
        def calc_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        curr = head
        
        while curr.next:
            next = curr.next
            gcd = calc_gcd(curr.val, next.val)
            curr.next = ListNode(gcd, next)
            curr = next
        
        return head

        
