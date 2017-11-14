# Source: https://leetcode.com/problems/replace-words/description/
# Author: Paulo Lemus
# Date  : 2017-11-14
# Info  : #648, Medium, 445 ms, 10.64%

# In English, we have a concept called root, which can be followed
# by some other words to form another longer word - let's call
# this word successor. For example, the root an, followed by other,
# which can form another word another.
#
# Now, given a dictionary consisting of many roots and a sentence.
# You need to replace all the successor in the sentence with
# the root forming it. If a successor has many roots can form it,
# replace it with the root with the shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"


# 445 ms, 10.64%
class Solution:
    def replaceWords(self, dict, sentence):
	"""
	:type dict: List[str]
	:type sentence: str
	:rtype: str
	"""
	prefix = set(dict)

	def getPrefix(word):
	    for i, __ in enumerate(word):
		if word[:i+1] in prefix:
		    return word[:i+1]
	    return word

	return ' '.join(list(map(getPrefix, sentence.split())))

