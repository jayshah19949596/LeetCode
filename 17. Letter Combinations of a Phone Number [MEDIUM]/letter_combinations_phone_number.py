"""
17. Letter Combinations of a Phone Number [MEDIUM]
https://leetcode.com/problems/letter-combinations-of-a-phone-number

### 1. Question Explanation:
----------------------------
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.


#### Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

#### Example 2:
Input: digits = ""
Output: []

#### Example 3:
Input: digits = "2"
Output: ["a","b","c"]

### 2. Solution Explanation:
----------------------------
APPROACH: DFS approach to get all letter combinations for a phone number

### 3. Complexity Analysis:
----------------------------
Time Complexity: O((4^N)*N) where N is the length of digits.
                 Note that 4 in this expression is referring to the maximum value length in the hash map,
                 and not to the length of the input.
Space Complexity: O(N)
"""
from typing import List


class Solution:
  
    digit2letter = {
        2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
        5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]
    }

    def letterCombinations(self, digits: str) -> List[str]:
        # return self.recurse_dfs(digits, 0, [], [])
        return self.iterative_dfs(digits)

    def iterative_dfs(self, digits):
        if not digits: return []
        results = [[]]

        for digit in digits:
            new_results = []
            for letter in Solution.digit2letter[digit]:
                for result in results:
                    new_results.append(result + [letter])
            results = new_results

        return ["".join(result) for result in results]

    def recurse_dfs(self, digits, idx, results, intermediate_answer):
        if idx == len(digits):
            final_answer = "".join(intermediate_answer)
            if final_answer: results.append(final_answer)
            return results

        for letter in Solution.digit2letter[digits[idx]]:
            self.recurse_dfs(digits, idx + 1, results, intermediate_answer + [letter])

        return results




class Solution:        
    def letterCombinations(self, digits: str) -> List[str]:
        num2letter = { 
            2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
            5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]
        }

        if not digits: return []
        cur_level = [[]]
        for num in digits:
            nxt_level = []
            for node_list in cur_level:
                for char in num2letter[int(num)]:
                    nxt_level.append(node_list+[char])
            cur_level = nxt_level
        return ["".join(node_list) for node_list in cur_level]
