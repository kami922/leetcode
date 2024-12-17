class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            sumVar = numbers[left] + numbers[right]
            if sumVar == target:
                res = [left+1,right+1]
                return res
            elif sumVar > target:
                right -= 1
            else:
                left += 1
                
            
            
        