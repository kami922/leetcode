class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i in range(0,len(nums)):
            indLen = len(index)
            for j in range(0+1,len(nums)):
                if nums[i] + nums[j] == target and indLen < 2 and j != i:
                    index.append(i)
                    index.append(j)
        return list(set(index))
            
         
        