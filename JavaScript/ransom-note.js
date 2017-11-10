/*
 * Source: https://leetcode.com/problems/ransom-note/description/
 * Author: Paulo Lemus
 * Date  : 2017-11-09
 */

/*
 * Given an arbitrary ransom note string and another string
 * containing letters from all the magazines, write a function
 * that will return true if the ransom note can be constructed
 * from the magazines ; otherwise, it will return false.
 *
 * Each letter in the magazine string can only be used once in your ransom note.
 *
 * Note:
 * You may assume that both strings contain only lowercase letters.
 *
 * canConstruct("a", "b") -> false
 * canConstruct("aa", "ab") -> false
 * canConstruct("aa", "aab") -> true
 */


/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const ransomLetters = _.countBy(ransomNote, (letter) => letter);
    const magLetters    = _.countBy(magazine,   (letter) => letter);

    return _.chain(ransomLetters)
        .keys()
        .every((key) => _.has(magLetters, key) && ransomLetters[key] <= magLetters[key])
        .value();
};

