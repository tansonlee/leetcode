class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 0:
            return []
        arr = [0 for _ in range(len(pref))]
        arr[0] = pref[0]

        curr = pref[0]
        for i in range(1, len(arr)):
            arr[i] = curr ^ pref[i]
            curr = curr ^ arr[i]
        
        return arr
        
