class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
        for index in range(lenNums-1):
            if nums[index] == nums[index+1]:
                nums[index] = nums[index]  * 2
                nums[index+1] = 0
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]  # Swap
                non_zero_index += 1
        return nums