/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const n = nums.length;
      const answer = new Array(n).fill(1);

      // Calculate prefix products
      for (let i = 1; i < n; i++) {
        answer[i] = answer[i - 1] * nums[i - 1];
      }

      // Calculate postfix products and multiply with prefix products
      let postfixProd = 1;
      for (let i = n - 1; i >= 0; i--) {
        answer[i] *= postfixProd;
        postfixProd *= nums[i];
      }

      return answer;
    
};