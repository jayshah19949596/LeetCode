"""
38. Count and Say [MEDIUM]
https://leetcode.com/problems/count-and-say/
### 1. Question:
----------------------------
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

### 2. Solution:
----------------------------
Iterate through the previous sequence.  When we see a
different number, append [1, num] to the new sequence.
When we see the same number increment its count.

### 3. Complexity Analysis:
----------------------------
Time - O(2^n), the sequence at worst doubles each step
Space - O(2^n)
"""
class Solution(object):
    def countAndSay(self, n: int) -> str:
        seq = [1]
        for i in range(1, n):
            new_seq = []
            for j, s in enumerate(seq):
                if not new_seq or new_seq[-1] != seq[j]:
                    new_seq.append(1)
                    new_seq.append(seq[j])
                elif new_seq[-1] == seq[j]:
                    new_seq[-2] += 1
            seq = new_seq
        return "".join([str(s) for s in seq])

