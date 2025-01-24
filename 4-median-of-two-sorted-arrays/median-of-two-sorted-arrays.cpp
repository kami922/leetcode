class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        int i = 0, j = 0;
        double m1 = 0, m2 = 0; 

        for (int count = 0; count <= (n + m) / 2; ++count) {
            m2 = m1; 
            if (i < n && j < m) {
                if (nums1[i] > nums2[j]) {
                    m1 = nums2[j];
                    ++j;
                } else {
                    m1 = nums1[i];
                    ++i;
                }
            } else if (i < n) {
                m1 = nums1[i];
                ++i;
            } else {
                m1 = nums2[j];
                ++j;
            }
        }

        if ((n + m) % 2 == 1) {
            return static_cast<double>(m1);
        } else {
            return (static_cast<double>(m1) + static_cast<double>(m2)) / 2.0;
        }
    }
};