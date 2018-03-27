/*
 * Source: https://leetcode.com/problems/jewels-and-stones/description/
 * Author: Paulo Lemus
 * Date  : 2018-03-25
 * Info  : #771, Easy
 */

/*
 * You're given strings J representing the types of stones that are jewels, 
 * and S representing the stones you have.  
 * Each character in S is a type of stone you have.  
 * You want to know how many of the stones you have are also jewels.
 * 
 * The letters in J are guaranteed distinct, and all characters in J and S are 
 * letters. 
 * Letters are case sensitive, so "a" is considered a different type of stone 
 * from "A".
 * 
 * Example 1:
 * 
 * Input: J = "aA", S = "aAAbbbb"
 * Output: 3
 * 
 * Example 2:
 * 
 * Input: J = "z", S = "ZZ"
 * Output: 0
 * 
 * Note:
 * 
 *     S and J will consist of letters and have length at most 50.
 *         The characters in J are distinct.
 */

#include <unordered_set>

class Solution {
public:
    int numJewelsInStones(std::string J, std::string S) {
        std::unordered_set<char> jewels(J.begin(), J.end());
        
        int jewel_count = 0;
        for(const char& ch : S) {
            if(jewels.find(ch) != jewels.end()) {
                jewel_count++;
            }
        }
        return jewel_count;
    }
};
