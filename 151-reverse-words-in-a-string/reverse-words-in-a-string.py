class Solution:
    def reverseWords(self, s: str) -> str:
        StrToList = s.split()
        resultStr = []
        for index in range(len(StrToList)-1,-1,-1):
            resultStr.append(StrToList[index])
            
        return " ".join(resultStr)