"""
https://leetcode.com/problems/product-of-array-except-self/

### 1. Question Explanation:
----------------------------
We are given a list schedule of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

#### Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

#### Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

##2. Solution Explanation:
----------------------------
All solutions iterate over the flattened and sorted schedule of all employees
If max_previous_end<employee_intervals[i].start then add Interval(max_previous_end, employee_intervals[i][0]) to results
New max_previous_end will be max(max_previous_end, employee_intervals[i].end)


##3. Complexity Analysis:
----------------------------
Time Complexity: O(N*LogN)
Space Complexity: O(N)
"""


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end



class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        employee_intervals = []

        for employee in schedule:
            for interval in employee:
                employee_intervals.append([interval.start, interval.end])

        employee_intervals.sort(key=lambda x: x[0])
        results, previous_end = [], employee_intervals[0][1]

        for i in range(0, len(employee_intervals)):
            if previous_end < employee_intervals[i][0]:
                results.append(Interval(previous_end, employee_intervals[i][0]))
            previous_end = max(previous_end, employee_intervals[i][1])

        return results
