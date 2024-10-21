class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(string, seen):
            if len(string) == 1:
                if string in seen:
                    return 0
                else:
                    return 1
            
            result = 0
            for i in range(len(string)):
                head = string[:i + 1]
                if head in seen:
                    continue
                seen.add(head)
                result = max(result, helper(string[i + 1:], seen) + 1)
                seen.remove(head)
            
            return result
        
        return helper(s, set())

                
        
