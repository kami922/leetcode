class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
    std::vector<int> answer(n, 1);

    // Calculate prefix products
    for (int i = 1; i < n; ++i) {
        answer[i] = answer[i - 1] * nums[i - 1];
    }

    // Calculate postfix products and multiply with prefix products
    int postfix_prod = 1;
    for (int i = n - 1; i >= 0; --i) {
        answer[i] *= postfix_prod;
        postfix_prod *= nums[i];
    }

    return answer;
        
    }
};