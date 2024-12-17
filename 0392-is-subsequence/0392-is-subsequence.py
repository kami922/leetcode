class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # Pointer for string 's'
        j = 0  # Pointer for string 't'

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s) 
                