/*
 * Source: https://leetcode.com/problems/sum-of-left-leaves/description/
 * Author: Paulo Lemus
 * Date  : 2017-11-09
 * Number: 404
 */

/*
 * Find the sum of all left leaves in a given binary tree.
 * 
 * Example:
 * 
 *     3
 *    / \
 *   9  20
 *     /  \
 *    15   7
 * 
 * There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	int sumOfLeftLeaves(TreeNode* root) {

		if(!root) return 0;
		else {
			int sum = 0;

			if(root->left && !root->left->left && !root->left->right) {
				sum += root->left->val;
			} else {
				sum += sumOfLeftLeaves(root->left);
			}
			sum += sumOfLeftLeaves(root->right);
			return sum;
		}
	}
};

