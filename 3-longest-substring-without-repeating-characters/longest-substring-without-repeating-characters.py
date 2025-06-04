class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return len(s)

        left = 0
        right = 0
        hashmap = {}
        maxLen = 0
        while right < len(s):
            if s[right] in hashmap:
                maxLen = max(maxLen,right-left)
                left = max(left,hashmap[s[right]]+1)

            hashmap[s[right]] = right
            right += 1
        return max(maxLen,right-left)