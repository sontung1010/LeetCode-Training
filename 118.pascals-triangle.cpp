/*
 * @lc app=leetcode id=118 lang=cpp
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        if (numRows == 0) {
            return triangle;
        }

        // first row is always 1
        triangle.push_back({1});

        for (int i = 1; i < numRows; i++) {
            vector<int> row;
            vector<int>& prevRow = triangle[i - 1];     // reference to previous row of triangle

            // first element is always 1
            row.push_back(1);

            for (int j = 1; j < prevRow.size(); j++) {
                row.push_back(prevRow[j - 1] + prevRow[j]);
            }

            // last element is always 1
            row.push_back(1);

            triangle.push_back(row);
        }

        return triangle;

    }
};
// @lc code=end

