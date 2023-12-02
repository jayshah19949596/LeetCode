"""
791. Custom Sort String [Medium]
https://leetcode.com/problems/custom-sort-string/description/

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

### 2. Solution Explanation:
----------------------------
The trick is to count the elements of "s". After we have some count[char] = (the number of occurrences of char in "s").
We can write these elements in the order we want. The order is "order" + (characters not in "order" in any sequence).


### 3. Complexity Analysis:
----------------------------
Time Complexity: O(order.length+s.length), the time it takes to iterate through S and T
Space Complexity: O(s.length). We count at most 26 different lowercase letters, but the final answer has the same length as T.

"""
from collections import defaultdict
class Solution:
    def prepare(self, order: str, s: str):
        order_set = set(order)
        string_freq = defaultdict(int)
        for i in range(len(s)):
            string_freq[s[i]] += 1

        return order_set, string_freq, []

    def customSortString(self, order: str, s: str) -> str:
        order_set, string_freq, results = self.prepare(order, s)

        for i in range(len(order)):
            if order[i] in string_freq:
                char_times = string_freq[order[i]]
                element = char_times * order[i]
                results.append(element)

        for char in string_freq:
            if char not in order_set:
                results.append(string_freq[char]*char)

        return "".join(results)
