"""
621. Task Scheduler [MEDIUM]
https://leetcode.com/problems/task-scheduler

### 1. Question Explanation:
----------------------------
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.


### 2. Solution Explanation:
----------------------------
1. The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.
2. Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.
3. Sort the array and retrieve the maximum frequency f_max. This frequency defines the max possible idle time: idle_time = (f_max - 1) * n.
4. Pick the elements in the descending order one by one. At each step, decrease the idle time by min(f_max - 1, f) where f is a current frequency. Remember, that idle_time is greater or equal to 0.
5. Return busy slots + idle slots:


### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(1)
"""
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n  # This defines the max possible idle times

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return len(tasks) + idle_time