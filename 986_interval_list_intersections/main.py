class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        result = []

        def intersection(i1, i2):
            if i1[0] > i2[0]:
                i1, i2 = i2, i1
            
            if i1[1] < i2[0]:
                return []
            if i1[1] <= i2[1]:
                return [i2[0], i1[1]]
            else:
                return i2
        
        while p1 < len(firstList) and p2 < len(secondList):
            inter = intersection(firstList[p1], secondList[p2])
            if inter:
                result.append(inter)
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
                
        return result


        
