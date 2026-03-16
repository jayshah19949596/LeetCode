"""
=================================
Approach-1: BruteForce
=================================
We are essentially checking every possible consecutive sequence that could sum to n.
This brute force works but is slow

Time: O(n^2)
"""
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        answer = 1   # n itself always counts

        for start in range(1, n):
            total_sum = 0
            for num in range(start, n):
                total_sum += num
                if total_sum == n:
                    answer += 1
                    break
                elif total_sum > n:
                    break

        return answer

"""
=========================================
Approach-2: SubOptimal Sliding Window
=========================================

Since the sequence must contain consecutive positive integers, the numbers always increase by 1.
So instead of trying all combinations, we can maintain a window of consecutive numbers and track their sum.

Since the numbers must be consecutive, we can treat the sequence as a sliding window.
We maintain two pointers representing the start and end of the window and track the running sum.
If the sum is smaller than n, we expand the window; if it is larger, we shrink it.
Whenever the sum equals n, we count it as a valid sequence.
Each pointer moves at most n times, giving O(n) time and O(1) space complexity.

Time: O(n)
"""
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        left = right = total_sum = 1
        answer = 0

        while left <= n:
            if total_sum == n:
                answer += 1
                total_sum -= left
                left += 1
            elif total_sum < n:
                right += 1
                total_sum += right
            else:
                total_sum -= left
                left += 1

        return answer
