class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        seen = set()

        def next_friend(curr):
            curr = curr % n + 1
            while curr in seen:
                curr = curr % n + 1
            return curr

        curr = 0
        while len(seen) < n - 1:
            for _ in range(k):
                curr = next_friend(curr)
            seen.add(curr)
        return next_friend(curr)

