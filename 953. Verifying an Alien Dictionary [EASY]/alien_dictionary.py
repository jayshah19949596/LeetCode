"""
953. Verifying an Alien Dictionary [EASY]
https://leetcode.com/problems/verifying-an-alien-dictionary

### 1. Question Explanation:
----------------------------
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.


#### Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

#### Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

#### Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


### 2. Solution Explanation:
----------------------------
On a high leve:
1] Mapping each character's position in the custom order.
2] Iteratively comparing each pair of consecutive words.
3] Checking character by character until it finds a discrepancy or confirms their correct ordering

Detailed Explanation:
This loop iterates through each pair of consecutive words in the words list. We take two words at a time: word_one and word_two.
initialize two indices, j and k, to track our position in word_one and word_two. The inner loop continues as long as there are characters left to compare in both words
If the character from word_one comes before the character from word_two in the custom order (order_map[char_one] < order_map[char_two]), we break out of the loop since we have determined that this part of the comparison is valid.
If both characters are equal (order_map[char_one] == order_map[char_two]), we increment both indices to compare the next characters.
If neither of these conditions holds (meaning char_one comes after char_two), we return False, indicating that the words are not sorted correctly.
After exiting the inner loop, if we have compared all characters and have not returned yet:
If word_one is longer than word_two, it means that they are not sorted correctly (since longer words should not come before shorter ones if they are identical up to the length of the shorter word). Thus, we return False.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N), where 'N' is total number of characters in words.
Space Complexity: O(1).
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: idx for idx, char in enumerate(order)}
        for i in range(len(words)-1):
            word_one, word_two = words[i], words[i+1]
            j, k = 0, 0
            while j<len(word_one) and k<len(word_two):
                char_one, char_two = word_one[j], word_two[k]
                if order_map[char_one] < order_map[char_two]:
                    break
                elif order_map[char_one] == order_map[char_two]:
                    j, k = j+1, k+1
                    continue
                else:
                    return False
            else:
                if len(word_one)>len(word_two): return False
        return True