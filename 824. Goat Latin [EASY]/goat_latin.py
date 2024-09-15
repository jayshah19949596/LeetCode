"""
824. Goat Latin
https://leetcode.com/problems/goat-latin

### 1. Question Explanation:
----------------------------

Topics
Companies
You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin


#### Example 1:
Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

#### Example 2:
Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


### 2. Solution Explanation:
----------------------------
???

### 3. Complexity Analysis:
----------------------------
Time - O(len(sentence))
Space - O(len(sentence))
"""
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        vowel = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        for i, word in enumerate(words):
            if word[0] in vowel:
                word = word+"ma"
            else:
                word = word[1:]+word[0]+"ma"
            char_a = (i+1)*"a"
            word = word+char_a
            words[i] = word
        return " ".join(words)