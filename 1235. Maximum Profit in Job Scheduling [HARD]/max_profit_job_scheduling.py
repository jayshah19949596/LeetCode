"""
1235. Maximum Profit in Job Scheduling [HARD]
https://leetcode.com/problems/maximum-profit-in-job-scheduling

### 1. Question Explanation:
----------------------------
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
If you choose a job that ends at time X you will be able to start another job that starts at time X.

#### Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

#### Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.

### 2. Solution Explanation:
----------------------------
Approach: Top-Down Dynamic Programming + Binary Search
Intuition
For each job, we will try two options:

Schedule this job and move on to the next non-conflicting job using binary search.
Skip this job and move on to the next available job.

### 3. Complexity Analysis:
----------------------------
Let N be the length of the jobs array.
Time complexity: O(N*LogN)
    - Sorting jobs according to their starting time will take O(N*LogN)
    - The time complexity for the recursion (with memoization) is equal to the number of times findMaxProfit is called times the average time of findMaxProfit.
    - The number of calls to findMaxProfit is 2^N because each non-memoized call will call findMaxProfit twice.
    - Each memoized call will take O(1) time while for the non-memoized call, we will perform a binary search that takes O(logN) time
    - Hence the time complexity will be O(N*LogN+N)

Space complexity: O(N)


"""
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(len(startTime))]
        jobs.sort(key=lambda x: x[0])
        memo = {}

        def get_max_profit(cur_job_idx):
            # Base case
            if cur_job_idx in memo: return memo[cur_job_idx]
            if cur_job_idx == len(jobs) - 1: return jobs[cur_job_idx][2]

            # Find profit when current job is included
            inclusive_profit = jobs[cur_job_idx][2]
            non_conflict_job_idx = -1

            # find next non-conflicting job using binary search
            left, right = cur_job_idx+1, len(jobs) - 1
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][0] >= jobs[cur_job_idx][1]:
                    non_conflict_job_idx = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if non_conflict_job_idx != -1:
                inclusive_profit += get_max_profit(non_conflict_job_idx)

            # Find profit when current job is excluded
            exclusive_profit = get_max_profit(cur_job_idx + 1)
            memo[cur_job_idx] = max(inclusive_profit, exclusive_profit)
            return memo[cur_job_idx]

        return get_max_profit(0)
