/*
 * @lc app=leetcode id=13 lang=cpp
 *
 * [13] Roman to Integer
 */

// @lc code=start
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<string, int> dict = {{"I", 1}, {"V", 5}, {"X", 10}, {"L", 50}, {"C", 100}, {"D", 500}, {"M", 1000}};

        int length = s.length();
        if (length == 0 || length > 15) {
            return -1;
        }

        int sum = 0;
        for (int i = 0; i < length; i++) {
            if (dict[string(1, s[i])] < dict[string(1, s[i+1])]) {
                sum += (dict[string(1, s[i+1])] - dict[string(1, s[i])]);
                i++;
            } else {
                sum += dict[string(1, s[i])];
            }
        }

        return sum;
    }
};
// @lc code=end

