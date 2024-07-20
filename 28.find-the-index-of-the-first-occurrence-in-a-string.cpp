/*
 * @lc app=leetcode id=28 lang=cpp
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.size() < needle.size()) {
            return -1;
        }

        for (int i = 0; i < haystack.size() - needle.size() + 1; i++) {
            string substr = haystack.substr(i, needle.size());
            if (substr == needle) {
                return i;
            }
        }

        return -1; 
    }
};
// @lc code=end

