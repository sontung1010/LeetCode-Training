/*
 * @lc app=leetcode id=507 lang=cpp
 *
 * [507] Perfect Number
 */

// @lc code=start
#include <iostream>
#include <vector>
// #include <cmath>

using namespace std;
    
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num < 0) {
            return false;
        }
        int sum {0}; 
        // find all the divisors
        vector<int> divisors;
        for (int i = 1; i <= sqrt(num); i++) {
            if (num % i == 0) {
                // cout << "i = " << i << endl;
                divisors.push_back(i);
                if (i != num/i) {
                    // cout << "num/i = " << num/i << endl; 
                    divisors.push_back(num/i);
                }
            }
        }

        for (int i = 0; i < divisors.size(); i++) {
            // cout << "divisors[" << i << "] = " << divisors[i] << endl;
            sum += divisors[i];
        }
        sum = sum - num;
        // cout << sum;
        // cout << num;
        return sum == num;
    }
};
// @lc code=end

