class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(left, right, mismatches):
            while left <= right:
                if s[left] != s[right]:
                    if mismatches == 0:
                        return False
                    else:
                        return helper(left + 1, right, mismatches - 1) or helper(left, right - 1, mismatches - 1)
                left += 1
                right -= 1
            return True

        return helper(0, len(s) - 1, 1)

        skipped = False
        front = 0
        back = len(s) - 1
        front_works = True

        while front < back:
            if s[front] != s[back]:
                if skipped:
                    front_works = False
                    break
                else:
                    skipped = True
                    front += 1
            else:
                front += 1
                back -= 1

        skipped = False
        front = 0
        back = len(s) - 1
        back_works = True

        while front < back:
            if s[front] != s[back]:
                if skipped:
                    back_works = False
                    break
                else:
                    skipped = True
                    back -= 1
            else:
                front += 1
                back -= 1
        
        return front_works or back_works 
            
        
