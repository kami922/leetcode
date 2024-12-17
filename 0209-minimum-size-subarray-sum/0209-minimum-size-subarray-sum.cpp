class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
    int sum = 0;
    int minLen = numeric_limits<int>::max(); // Use numeric_limits for infinity
    int windowStart = 0;

    for (int end = 0; end < n; ++end) {
        sum += nums[end];

        while (sum >= target) {
            minLen = min(minLen, end - windowStart + 1);
            sum -= nums[windowStart];
            windowStart++;
        }
    }

    return (minLen == numeric_limits<int>::max()) ? 0 : minLen;
}

int main() {
    vector<int> nums = {2, 3, 1, 2, 4, 3};
    int target = 7;

    int result = minSubArrayLen(target, nums);

    cout << "Minimum subarray length: " << result << endl;

    return 0;
    }
};