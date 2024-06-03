"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            v = Node(insertVal)
            v.next = v
            return v
        
        curr = head
        insert_after = head
        maximum = head 
        while True:
            if curr.val > curr.next.val:
                maximum = curr
            if curr.val <= insertVal <= curr.next.val:
                insert_after = curr
                break
            curr = curr.next

            # Full circle with no insert
            if curr == head:
                insert_after = maximum
                break

        next = insert_after.next
        insert_after.next = Node(insertVal)
        insert_after.next.next = next
        return head
        

