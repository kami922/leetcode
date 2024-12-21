class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strList = s.split()
        result = len(strList[-1])
        return result