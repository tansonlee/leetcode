class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Determine where the last M P G are and their counts
        last_m = 0
        qty_m = 0
        last_p = 0
        qty_p = 0
        last_g = 0
        qty_g = 0
        for i in range(len(garbage)):
            for g in garbage[i]:
                if g == "M":
                    last_m = i
                    qty_m += 1
                elif g == "P":
                    last_p = i
                    qty_p += 1
                elif g == "G":
                    last_g = i
                    qty_p += 1
        
        result = 0

        # Metal
        for i in range(last_m):
            result += travel[i]
        result += qty_m

        # Paper 
        for i in range(last_p):
            result += travel[i]
        result += qty_p

        # Glass 
        for i in range(last_g):
            result += travel[i]
        result += qty_g

        return result
