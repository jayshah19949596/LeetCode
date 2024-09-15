"""
437. Path Sum III [MEDIUM]
https://leetcode.com/problems/path-sum-iii

### 1. Question Explanation:
----------------------------
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

### 2. Solution:
----------------------------
References: https://leetcode.com/problems/subarray-sum-equals-k/description/

###  3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node: return

            curr_sum += node.val
            if curr_sum == k: count += 1
            if curr_sum - k in sum_seen : count += sum_seen[curr_sum - k]
            sum_seen[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            # Remove the current sum from the hashmap in order
            # not to use it during the parallel subtree processing
            sum_seen[curr_sum] -= 1

        count, k = 0, sum
        sum_seen = defaultdict(int)
        preorder(root, 0)
        return count
