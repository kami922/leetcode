class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            chat1 = s[i]
            chat2 = s[i+1]
            chat3 = s[i+2]
            if chat1 != chat2 and chat2 != chat3 and chat1 != chat3:
                count += 1
        return count