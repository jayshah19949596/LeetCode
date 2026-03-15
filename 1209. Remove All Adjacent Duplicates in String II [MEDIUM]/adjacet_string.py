"""
We use a stack where each entry stores a character and its current consecutive count. 
While scanning the string, if the current character matches the top of the stack, we increment the count. 
If that count reaches k, we remove that entry from the stack, which simulates deleting those adjacent duplicates. 
If the current character is different, we start a new stack entry. At the end, we rebuild the string from the remaining stack contents. 
This handles chain reactions naturally because once a group is removed, the previous group becomes the new top of the stack.
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []   # [char, count]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        result = []
        for ch, count in stack:
            result.append(ch * count)

        return "".join(result)
