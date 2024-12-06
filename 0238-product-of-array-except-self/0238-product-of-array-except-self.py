class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Calculate postfix products and multiply with prefix products
        postfix_prod = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix_prod
            postfix_prod *= nums[i]

        return answer

            
        