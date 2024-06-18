class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
                