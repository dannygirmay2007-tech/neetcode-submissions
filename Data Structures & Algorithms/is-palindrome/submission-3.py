class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.rstrip("?")
        s = s.replace(",", '')
        s = s.replace("'", '')
        s = s.replace(".", '')
        s = s.replace(":", '')
        s = s.replace(" ", '')
        s = s.upper()
        if s == s[::-1]:
            return True
        else:
            return False
        