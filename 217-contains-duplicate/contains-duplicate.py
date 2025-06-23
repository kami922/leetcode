class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for index in range(len(nums)):
            if nums[index] in check:
                return True
            else:
                check[nums[index]] = 1
        return False