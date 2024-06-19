class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def count_good(threshold):
            result = 0
            idx = 0
            while idx < len(bloomDay):
                while idx < len(bloomDay) and bloomDay[idx] > threshold:
                    idx += 1

                curr = 0
                while idx < len(bloomDay) and bloomDay[idx] <= threshold:
                    curr += 1
                    idx += 1
                result += (curr // k)
            return result 

        bottom = min(bloomDay)
        top = max(bloomDay)
        result = -1
        while bottom <= top:
            mid = (bottom + top) // 2
            if count_good(mid) >= m:
                top = mid - 1
                result = mid
            else:
                bottom = mid + 1

        return result
        

        



