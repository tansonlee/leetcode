# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        flippedA, flippedB = False, False

        while True:
            if a == b:
                return a
            
            if a.next:
                a = a.next
            elif flippedA and flippedB:
                return None 
            else:
                a = headB
                flippedA = True
            
            if b.next:
                b = b.next
            elif flippedA and flippedB:
                return None 
            else:
                b = headA
                flippedB = True
        
