class Solution:
    def checkValidString(self, s):
        @functools.cache
        def helper(s, opens):
            if opens < 0:
                return False
            if len(s) == 0:
                return opens == 0
            if s[0] == '(':
                return helper(s[1:], opens + 1)
            if s[0] == ')':
                return helper(s[1:], opens - 1)
            if s[0] == '*':
                return helper(s[1:], opens + 1) \
                    or helper(s[1:], opens) \
                    or helper(s[1:], opens - 1)
        
        return helper(s, 0)

