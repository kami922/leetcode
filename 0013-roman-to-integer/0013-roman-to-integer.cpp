class Solution {
public:
    int romanToInt(string s) {
         std::unordered_map<char, int> roman_map = {
            {'I', 1}, {'V', 5}, {'X', 10},
            {'L', 50}, {'C', 100}, {'D', 500},
            {'M', 1000}
        };
        
        // Length of the given string
        int n = s.length();
        
        // This variable will store result
        int num = roman_map[s[n - 1]];
        
        // Loop for each character from right to left
        for (int i = n - 2; i >= 0; --i) {
            // Check if the character at right of the current character is bigger or smaller
            if (roman_map[s[i]] >= roman_map[s[i + 1]]) {
                num += roman_map[s[i]];
            } else {
                num -= roman_map[s[i]];
            }
        }
        
        return num;
    }
};