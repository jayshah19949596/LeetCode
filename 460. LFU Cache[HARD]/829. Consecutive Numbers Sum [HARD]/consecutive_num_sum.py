"""
Approach-1: BruteForce
We are essentially checking every possible consecutive sequence that could sum to n.
This brute force works but is slow
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
