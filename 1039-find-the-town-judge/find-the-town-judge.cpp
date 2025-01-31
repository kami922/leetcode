class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
         vector<int> trust_received(n + 1, 0); // Initialize with 0 trust received
        vector<int> trust_given(n + 1, 0);     // Initialize with 0 trusts given

        // Process trust relationships
        for (const auto& relation : trust) {
            int giver = relation[0];
            int receiver = relation[1];
            trust_given[giver]++;
            trust_received[receiver]++;
        }

        // Find the potential judge
        for (int person = 1; person <= n; ++person) {
            if (trust_given[person] == 0 && trust_received[person] == n - 1) {
                return person; 
            }
        }

        return -1; // No judge found
        
    }
};