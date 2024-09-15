"""
791. Custom Sort String [Medium]
https://leetcode.com/problems/custom-sort-string/

### 1. Question Explanation:
-----------------
Let's first write to our answer the elements of "s" that occur in "order", in sequence of "order".
After, we'll write any elements of "s" we didn't write. This obviously keeps all the ordering relationships we wanted.

In the second write, the order doesn't matter because those elements aren't in "order", so there are no ordering relationships these elements have to satisfy.

#### Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

#### Example 2:
Input: order = "cbafg", s = "abcd"
Output: "cbad"
"""
from collections import Counter

"""
=============================================
APPROACH-1: Custom Comparator with Sorting
=============================================
### 1. Solution Explanation:
----------------------------
Create Custom comparator to be used with Sorting.

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N*LogN)
Space Complexity: O(N)
""""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        custom_comparator_values = defaultdict(int)

        for i, char in enumerate(order):
            custom_comparator_values[char] = i

        return ''.join(sorted(list(s), key=lambda x: custom_comparator_values[x]))

"""
=============================================
APPROACH-2: Frequency Table and Counting
=============================================
1. We count the elements of "s" in a frequency table.
2. We write the elements of "order" in the order they appear in "s".
3. We write the elements of "s" we didn't write in any order.

### 1. Solution Explanation:
----------------------------
The trick is to count the elements of "s". After we have some count[char] = (the number of occurrences of char in "s").
We can write these elements in the order we want. The order is "order" + (characters not in "order" in any sequence).


### 2. Complexity Analysis:
----------------------------
Time Complexity: O(order.length+s.length), the time it takes to iterate through S and T
Space Complexity: O(s.length). We count at most 26 different lowercase letters, but the final answer has the same length as T.
"""
class Solution:

    def customSortString(self, order: str, s: str) -> str:
        results, s_counter, order_set = [], Counter(s), set([])

        for char in order:
            if char in s_counter:
                results.append(char * s_counter[char])
                order_set.add(char)

        for char in s_counter:
            if char not in order_set:
                results.append(char * s_counter[char])

        return "".join(results)