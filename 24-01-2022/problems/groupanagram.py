'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''


def groupAnagrams( strs):
	anagrams = {}
	
	for s in strs:
		s_sorted = "".join(sorted(s))
		if s_sorted not in anagrams:
			anagrams[s_sorted] = []
		anagrams[s_sorted].append(s)
		
	return [list(value) for key, value in anagrams.items()]

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

