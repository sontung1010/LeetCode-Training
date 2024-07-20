/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>    // for reverse

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string str = to_string(x); string reverse_str = to_string(x);
        reverse(reverse_str.begin(), reverse_str.end());
        if (str == reverse_str) {
            return true;
        } else {
            return false;
        }

    }
};
// @lc code=end

