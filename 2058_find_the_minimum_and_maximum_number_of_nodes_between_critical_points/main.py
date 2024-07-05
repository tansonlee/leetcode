# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []

        def get_critical_points(curr, prev, curr_index):
            if curr is None or curr.next is None:
                return
            if prev.val < curr.val and curr.val > curr.next.val:
                critical_points.append(curr_index)
            elif prev.val > curr.val and curr.val < curr.next.val:
                critical_points.append(curr_index)
            get_critical_points(curr.next, curr, curr_index + 1)
        
        get_critical_points(head.next, head, 1)

        if len(critical_points) < 2:
            return [-1, -1]
        
        max_dist = critical_points[-1] - critical_points[0]
        min_dist = inf
        for i in range(len(critical_points) - 1):
            min_dist = min(min_dist, critical_points[i + 1] - critical_points[i])
        
        return [min_dist, max_dist]

            
        
