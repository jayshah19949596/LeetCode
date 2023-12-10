"""
https://leetcode.com/problems/valid-palindrome-iii

### 1. Question Explanation:
----------------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

### 2. Solution Explanation:
Solution taken from https://leetcode.com/problems/valid-palindrome-iii/solutions/4262752/python3-two-pointers-bfs/

### 3. Complexity Analysis:
----------------------------
Time complexity: O(N^2).
Each node is characterized by (l,r), and 0 <= l < r < len(s).
Assume k = N, there is a total of (N^2/2) possible

Space complexity: O(N^2). The visited array and the queue list can hold (N^2) nodes.
"""
from collections import deque


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # queue holds a tuple of `l` and `r`, and the depth `curr_k`.
        queue, visited = deque([(0, len(s) - 1, 0)]), set([])

        while queue:
            l, r, curr_k = queue.popleft()

            # If the budget is exceeded return False
            if curr_k > k: return False

            # Shave off the two ends of s[l:r+1] until end characters
            # don't match. Each graph node is defined by (l,r)
            # where s[l] != s[r].
            while s[l] == s[r]:
                l, r = l+1, r-1
                # if you reach the end node, you've found a k-palindrome
                if l >= r: return True

            # append the two new nodes to the queue.
            for new_l, new_r in [(l+1, r), (l, r-1)]:
                if (new_l, new_r) not in visited:
                    queue.append((new_l, new_r, curr_k+1))
                    visited.add((new_l, new_r))
