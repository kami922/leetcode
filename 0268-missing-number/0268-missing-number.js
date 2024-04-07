/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const N = nums.length;
    const summation = (N * (N + 1)) / 2;

    // Summation of all array elements:
    const s2 = nums.reduce((acc, num) => acc + num, 0);

    const missingNum = summation - s2;
    return missingNum;
};