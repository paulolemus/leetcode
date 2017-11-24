/*
 * Source: https://leetcode.com/problems/ransom-note/description/ 
 * Author: Paulo Lemus
 * Date  : 2017-11-24
 * Info  : #383, Easy, 23 ms, 71.34%
 *
 * Given an arbitrary ransom note string and another string containing 
 * letters from all the magazines, write a function that will return 
 * true if the ransom note can be constructed from the magazines 
 * ; otherwise, it will return false.
 * 
 * Each letter in the magazine string can only be 
 * used once in your ransom note.
 * 
 * Note:
 * You may assume that both strings contain only lowercase letters.
 * 
 * canConstruct("a", "b") -> false
 * canConstruct("aa", "ab") -> false
 * canConstruct("aa", "aab") -> true
 */


#include <string>
#include <vector>
class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        std::vector<int> letter_counts(26, 0);
        
        for(auto& ch : magazine) {
            letter_counts[ch - 'a']++;
        }
        
        for(auto& ch : ransomNote) {
            if(--letter_counts[ch - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};

