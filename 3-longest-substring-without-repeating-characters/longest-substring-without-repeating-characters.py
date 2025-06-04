class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = r = 0
        maxLen = 0
        hashmap = {}
        while r< len(s):
            if s[r] in hashmap:
                maxLen = max(maxLen,r-l) 
                l = max(l,hashmap[s[r]]+1)
            hashmap[s[r]] = r
            r += 1
        return max(maxLen,r-l)

