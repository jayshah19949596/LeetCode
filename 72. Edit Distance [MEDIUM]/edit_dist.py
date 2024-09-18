"""
==============================================
APPROACH-1: Brute Force with Recursion (TLE)
==============================================
### 1. Solution Explanation:
----------------------------
Base Cases:
- If we reach the end of word1, the remaining length of word2 represents how many insertions are needed.
- If we reach the end of word2, the remaining length of word1 represents how many deletions are needed.
Recursive Cases:
- If the current characters of both strings match (word1[i] == word2[j]), we move to the next characters without adding any operation cost.
- If they do not match, we calculate the cost for each operation (insert, delete, replace) and take the minimum among them.

### 2. Complexity Analysis:
----------------------------
Time: O(3**max(m,n))
Space:O(max(m,n))
"""
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        def recurse(i: int, j: int) -> int:
            # If we have reached the end of word1
            if i == len(word1):
                return len(word2) - j  # Remaining characters in word2 need to be inserted

            # If we have reached the end of word2
            if j == len(word2):
                return len(word1) - i  # Remaining characters in word1 need to be deleted

            # If characters are the same, move to the next characters
            if word1[i] == word2[j]:
                return recurse(i + 1, j + 1)

            # If characters are different, consider all possibilities
            insert_op = recurse(i, j + 1)   # Insert operation
            delete_op = recurse(i + 1, j)   # Delete operation
            replace_op = recurse(i + 1, j + 1)  # Replace operation

            return 1 + min(insert_op, delete_op, replace_op)

        return recurse(0, 0)

"""
==============================================
APPROACH-1: Recursion with Memoization (TLE)
==============================================

### 1. Solution Explanation:
----------------------------
We added a dictionary memo to store the results of previous computations.
Before performing any recursive call, we check if the current state (i, j) is already present in the memo dictionary.
If it is, we return the stored value.
If not, we proceed with the recursive call and store the result in the memo dictionary before returning it.
By memoizing the results, we avoid redundant calculations and significantly improve the time complexity of the solution.


### 2. Complexity Analysis:
----------------------------
Time: O(mn). With memoization, the time complexity is reduced to
             O(mn), where m and n  are the lengths of word1 and word2, respectively.
             This is because each state (i, j) is computed only once.

Space: O(max(m,n)). The space complexity remains the same as the recursive solution
"""
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}
        def recurse(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            # If we have reached the end of word1
            if i == len(word1):
                memo[(i, j)] = len(word2) - j
                return memo[(i, j)]

            # If we have reached the end of word2
            if j == len(word2):
                memo[(i, j)] = len(word1) - i
                return memo[(i, j)]

            # If characters are the same, move to the next characters
            if word1[i] == word2[j]:
                memo[(i, j)] = recurse(i + 1, j + 1)
                return memo[(i, j)]

            # If characters are different, consider all possibilities
            insert_op = recurse(i, j + 1)   # Insert operation
            delete_op = recurse(i + 1, j)   # Delete operation
            replace_op = recurse(i + 1, j + 1)  # Replace operation

            memo[(i, j)] = 1 + min(insert_op, delete_op, replace_op)
            return memo[(i, j)]
        return recurse(0, 0)
