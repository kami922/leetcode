class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squareNums = []
        for i in nums:
            squareNums.append(i**2)
        squareNums.sort()        
        return squareNums