class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int N = nums.size();
        int summation = (N * (N + 1)) / 2;

        // Summation of all array elements:
        int s2 = 0;
        for (int num : nums) {
            s2 += num;
        }

        int missingNum = summation - s2;
        return missingNum;
        
    }
};