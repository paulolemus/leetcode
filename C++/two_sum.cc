/*
 * Source: https://leetcode.com/submissions/detail/129187691/
 * Author: Paulo Lemus
 * Date  : 2017-11-21
 * Info  : #1, Easy, 6 ms, 77.56%
 * 
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * 
 * Example:
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 */


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> matches;
        
        int i = 0;
        for(auto const& num : nums) {
            if(matches.count(num)) {
                return vector<int>{matches[num], i};
            }
            matches[target-num] = i;
            i++;
        }
    }
};

