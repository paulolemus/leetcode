/*
 * Source: https://leetcode.com/problems/hamming-distance/description/
 * Author: Paulo Lemus
 * Date  : 2017-11-01
 */

/*
 * The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
 * 
 * Given two integers x and y, calculate the Hamming distance.
 * 
 * Note:
 * 0 ≤ x, y < 231.
 * 
 * Example:
 * 
 * Input: x = 1, y = 4
 * 
 * Output: 2
 * 
 * Explanation:
 * 1   (0 0 0 1)
 * 4   (0 1 0 0)
 *        ↑   ↑
 * 
 * The above arrows point to positions where the corresponding bits are different.
 */

class HammingDistance {
    public int hammingDistance(int x, int y) {
        
        int count = 0;
        int bits  = x^y;
        
        while(bits != 0) {
            count += bits & 1;
            bits >>= 1;
        }
        return count;
    }
}

