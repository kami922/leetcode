class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        summation = (N * (N + 1)) //2

        # Summation of all array elements:
        s2 = sum(nums)

        missingNum = summation - s2
        return missingNum
