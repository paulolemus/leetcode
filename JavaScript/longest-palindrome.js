/*
 * Source: https://leetcode.com/problems/longest-palindrome/description/
 * Author: Paulo Lemus
 * Date  : 2017-11-09
 * Number: 409
 */

/*
 * Given a string which consists of lowercase or uppercase letters,
 * find the length of the longest palindromes that can be built with those letters.
 *
 * This is case sensitive, for example "Aa" is not considered a palindrome here.
 *
 * Note:
 * Assume the length of given string will not exceed 1,010.
 *
 * Example:
 *
 * Input:
 * "abccccdd"
 *
 * Output:
 * 7
 *
 * Explanation:
 * One longest palindrome that can be built is "dccaccd", whose length is 7.
 */


/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {

	let foundSingleton = false;
	return _.chain(s)
		.countBy((letter) => letter)
		.map((val, key) => val)
		.reduce((memo, num) => {
			if(num % 2 !== 0) {
				if(foundSingleton) {
					return memo + num - 1;
				} else {
					foundSingleton = true;
				}
			}
			return memo + num;
		}, 0)
		.value();
};
