"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_seen = set([p])
        q_seen = set([q])

        curr_p = p
        curr_q = q

        while True:
            if curr_p in q_seen:
                return curr_p
            if curr_q in p_seen:
                return curr_q
            
            if curr_p.parent is not None:
                curr_p = curr_p.parent
            if curr_q.parent is not None:
                curr_q = curr_q.parent

            p_seen.add(curr_p)
            q_seen.add(curr_q)
            
        
