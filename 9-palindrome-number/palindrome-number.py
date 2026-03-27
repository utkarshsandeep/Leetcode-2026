class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        output = ""

        i = 0
        while i < len(s):
            output = s[i] + output
            i += 1

        if s == output:
            return True
        else:
            return False