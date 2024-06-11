class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = {}
        for i, n in enumerate(arr2):
            index[n] = i

        def key_fn(element):
            if element in index:
                return index[element]
            else:
                return 1000 + element
        
        arr1.sort(key=key_fn)
        return arr1

        
