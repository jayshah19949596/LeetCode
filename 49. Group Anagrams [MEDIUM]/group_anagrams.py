"""
https://leetcode.com/problems/anagrams/
Given an array of strings, group anagrams together.

Sort the letters in each word.  Use sorted words
as dictionary keys, values are unsorted words.
Anagrams have equivalent sorted words.
Time - O(k log k * n) for n words of length k
Space - O(k * n)
"""
from collections import defaultdict

class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_words = defaultdict(list)

        for word in strs:
            letter_list = [c for c in word]
            letter_list.sort()
            sorted_word = "".join(letter_list)
            sorted_words[sorted_word].append(word)

        return list(sorted_words.values())
    
"""
Time Complexity: O(NK)O(NK), where NN is the length of strs, 
and KK is the maximum length of a string in strs. 
Counting each string is linear in the size of the string, and we count every string.
Space Complexity: O(NK)O(NK), the total information content stored in ans.
"""
class Solution():
    def groupAnagrams(self, strs):
        ouput = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            ouput[tuple(char_count)].append(word)
        return list(ouput.values())
