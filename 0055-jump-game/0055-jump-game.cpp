class Solution {
public:

    bool canJump(const std::vector<int>& nums) {
        int gas = 0;
        for (int n : nums) {
            if (gas < 0) {
                return false;
            }
            gas = std::max(gas, n) - 1;
        }
        return true;
    }
};