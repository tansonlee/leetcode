# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # First find the total length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Determine the length of each part
        base_length = length // k
        num_additional_length = length - (base_length * k)
        num_base_length = k - num_additional_length

        def add_sublists(result, length, count, head):
            for _ in range(length):
                # Nothing left in the list.
                if not head:
                    result.append(None)
                    continue

                result.append(head)
                prev = None
                for _ in range(count):
                    prev = head
                    head = head.next
                    
                # Break off the list from the rest.
                prev.next = None
            return head

        result = []
        count = 0
        curr = head

        # Add all the lists that are base_length + 1 in size
        curr = add_sublists(result, num_additional_length, base_length + 1, curr)
        
        # Add the remaining lists
        curr = add_sublists(result, num_base_length, base_length, curr)
        
        return result

        
