class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        def merge(arr1, arr2):
            result = []
            p1 = 0
            p2 = 0
            while p1 < len(arr1) and p2 < len(arr2):
                print(arr1[p1], arr2[p2])
                if arr1[p1] == arr2[p2]:
                    result.append(arr1[p1])
                    p1 += 1
                    p2 += 1
                elif arr1[p1] < arr2[p2]:
                    p1 += 1
                else:
                    p2 += 1
            return result

        result = arrays[0]

        for i in range(1, len(arrays)):
            result = merge(result, arrays[i])
        
        return result


