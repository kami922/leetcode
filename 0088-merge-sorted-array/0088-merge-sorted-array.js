function merge(nums1, m, nums2, n) {
    // Copy nums2 to the end of nums1
    for (let i = 0; i < n; i++) {
        nums1[m + i] = nums2[i];
    }

    // Sort the entire nums1 array
    nums1.sort((a, b) => a - b);
}