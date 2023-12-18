"""
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

### 1. Question Explanation:
----------------------------
You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.
You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.
Each day, until all tasks have been completed, you must either:
Complete the next task from tasks, or
Take a break.
Return the minimum number of days needed to complete all tasks.

#### Example 1:

Input: tasks = [1,2,1,2,3,1], space = 3
Output: 9
Explanation:
One way to complete all tasks in 9 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
Day 7: Take a break.
Day 8: Complete the 4th task.
Day 9: Complete the 5th task.
It can be shown that the tasks cannot be completed in less than 9 days.

#### Example 2:

Input: tasks = [5,8,8,5], space = 2
Output: 6
Explanation:
One way to complete all tasks in 6 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
It can be shown that the tasks cannot be completed in less than 6 days.

### 2. Solution Explanation:
----------------------------
Approach: Simulating the scheduler.
Have a variable "day_number" to keep track of number of days
Have a variable "last_seen" to keep track of the day task was last seen.
Whenever difference between the day task was last seen and current day for task was less than space, then add the diff to day_number.

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(N)
"""

from collections import defaultdict
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day_number, last_seen = 0, defaultdict(int)
        for idx, task in enumerate(tasks):
            if task in last_seen:
                last_seen_day = last_seen[task]
                no_of_days_between_last_and_now = day_number - last_seen_day
                if no_of_days_between_last_and_now <= space: day_number += space - no_of_days_between_last_and_now
            day_number += 1
            last_seen[task] = day_number
        return day_number
