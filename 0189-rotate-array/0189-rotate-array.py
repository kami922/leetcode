class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # end = len(nums) - k # 7-3 = 4
        # # nums = nums[end:] + nums[:end]
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

        
        
        
        