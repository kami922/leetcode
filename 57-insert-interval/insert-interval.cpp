class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
         // Add the new interval
        intervals.push_back(newInterval);

        // Sort intervals based on the start time
        sort(intervals.begin(), intervals.end());

        // Result vector to store merged intervals
        vector<vector<int>> res;
        res.push_back(intervals[0]);

        // Iterate through the intervals and merge if necessary
        for (int i = 1; i < intervals.size(); ++i) {
            if (res.back()[1] >= intervals[i][0]) {
                // Merge intervals
                res.back()[1] = max(res.back()[1], intervals[i][1]);
            } else {
                // Add non-overlapping interval
                res.push_back(intervals[i]);
            }
        }

        return res;
    }
};