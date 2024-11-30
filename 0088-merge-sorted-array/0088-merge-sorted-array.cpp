class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Copy nums2 to the end of nums1
    for (int i = 0; i < n; ++i) {
        nums1[m + i] = nums2[i];
    }

    // Sort the entire nums1 array
    std::sort(nums1.begin(), nums1.end());
        
    }
};