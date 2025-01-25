class Solution {
public:
     bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> seen; // To store the value and its last index

        for (int i = 0; i < nums.size(); ++i) {
            if (seen.find(nums[i]) != seen.end() && i - seen[nums[i]] <= k) {
                return true;
            }
            seen[nums[i]] = i; // Update the index of the current value
        }

        return false;
    }
};