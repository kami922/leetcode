class Solution:
    def isPalindrome(self,num: int) -> bool:
        st = str(num)
        return st == st[::-1]