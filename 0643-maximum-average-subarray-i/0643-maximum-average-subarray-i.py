class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = []
        start=_sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            
            if i >= k-1:
                avg.append(_sum/k)
                _sum -= nums[start]
                start += 1
                
        return max(avg)
        