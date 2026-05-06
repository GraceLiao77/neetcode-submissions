class Solution:
    def isPalindrome(self, s: str) -> bool:

        prepoint = 0
        reversepoint = len(s)-1

        while prepoint < reversepoint:
            if not s[prepoint].isalnum():
                prepoint += 1
                continue
            if not s[reversepoint].isalnum():
                reversepoint -= 1
                continue
            if s[prepoint].upper() == s[reversepoint].upper():
                prepoint += 1
                reversepoint -= 1
            else:
                return False
        return True



