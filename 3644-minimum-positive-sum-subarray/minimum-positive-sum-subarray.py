
import sys
class Solution:
    from typing import List
import sys

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minSum = sys.maxsize
        found = False
        for length in range(l, r + 1):
            if length > n:
                continue
            currentSum = sum(nums[i] for i in range(length))
            if currentSum > 0:
                minSum = min(minSum, currentSum)
                found = True
            for i in range(length, n):
                currentSum += nums[i] - nums[i - length]
                if currentSum > 0:
                    minSum = min(minSum, currentSum)
                    found = True
        return minSum if found else -1