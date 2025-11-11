class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join(c.lower() for c in s if c.isalnum()).replace(" ", "")
        temp_list = [i for i in temp if True]

        return True if temp_list == temp_list[-1: : -1] else False
        