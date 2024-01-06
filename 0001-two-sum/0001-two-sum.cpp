class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numMap; // Map to store (target - nums[i]) and its index

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];

            // Check if the complement is already in the map
            if (numMap.find(complement) != numMap.end()) {
                // Return the indices of the two numbers
                return {numMap[complement], i};
            }

            // Store the current number and its index in the map
            numMap[nums[i]] = i;
        }

        // Return an empty vector if no solution is found
        return {};
        
    }
};