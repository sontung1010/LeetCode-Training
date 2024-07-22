/*
 * @lc app=leetcode id=14 lang=cpp
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // return empty string if the input vector is empty 
        if (strs.empty()) {
            return "";
        }

        // start with the first string as the initial prefix
        string prefix = strs[0];
        // iterate through the remaining strings
        for (int i = 1; i < strs.size(); i++) {
            // find the common prefix between the current prefix and the current string
            while (strs[i].find(prefix) != 0) {
                // reduce the length of the prefix
                prefix = prefix.substr(0, prefix.size() - 1);
                if (prefix.empty()) {
                    return "";
                }
            }
        } 

        return prefix;
    }
};
// @lc code=end

