from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        strInt = ""
        for i in digits:
            strInt += str(i)
            
            
        strInt = int(strInt)
        strInt += 1
        # strInt = str(strInt)
        for i in str(strInt):
            res.append(int(i))
        return list(res)
        
        