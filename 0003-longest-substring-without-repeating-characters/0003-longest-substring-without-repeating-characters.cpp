class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
    if (n <= 1) {
        return n;
    }

    int left = 0, right = 0;
    int maxLength = 0;
    std::unordered_map<char, int> charIndex;

    while (right < n) {
        char ch = s[right];
        if (charIndex.count(ch)) {
            left = std::max(left, charIndex[ch] + 1);
        }
        charIndex[ch] = right;
        maxLength = std::max(maxLength, right - left + 1);
        right++;
    }

    return maxLength;
        
    }
};