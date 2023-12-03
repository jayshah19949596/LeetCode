"""
https://leetcode.com/problems/stickers-to-spell-word

### 1. Question Explanation:
----------------------------
We are given "n" different types of "stickers". Each sticker has a lowercase English word on it.
You would like to spell out the given string "target" by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

#### Example 1:
Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

#### Example 2:
Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.

### 2. Solution Explanation:
----------------------------
Recursively calculate the new target by selecting one sticker at a time 
And select minimum number of stickers used to reach the target;.

### 3. Complexity Analysis:
----------------------------
Time - O(stickers.length * target.length): 
The dfs function calls itself stickers.length times upto target.length

Space - O(N)
"""
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        self.global_min_answer = float("inf")
        result = self.dfs(stickers, target, {}, 0)
        return result if result != float("inf") else -1

    @staticmethod
    def get_new_target(target, sticker):
        new_target = target

        for char in sticker:
            idx_to_remove = new_target.find(char)
            if idx_to_remove != -1:
                new_target = new_target[:idx_to_remove] + new_target[idx_to_remove + 1:]

        return new_target

    def dfs(self, stickers, target, memo, sticker_used):
        if sticker_used >= self.global_min_answer :
            return float("inf")

        if target == "":
            self.global_min_answer = min(self.global_min_answer, sticker_used)
            return sticker_used

        if (sticker_used, target) in memo:
            return memo[(sticker_used, target)]

        min_answer = float("inf")

        for sticker_idx, current_sticker in enumerate(stickers):
            new_target = Solution.get_new_target(target, current_sticker)
            if new_target != target:
                answer = self.dfs(stickers, new_target, memo, sticker_used + 1)
                min_answer = min(min_answer, answer)

        memo[(sticker_used, target)] = min_answer
        return min_answer
