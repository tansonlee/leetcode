class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = [n % k for n in arr]
        counts = Counter(mods)

        for n in counts:
            if n == 0:
                if counts[n] % 2 == 1:
                    return False
            else:
                # Find the compliment
                compliment = k - n
                if counts[n] != counts[compliment]:
                    return False
        
        return True
