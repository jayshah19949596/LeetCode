"""
https://leetcode.com/problems/moving-average-from-data-stream

### 1. Question Explanation:
----------------------------
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Implement the MovingAverage class:
MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

#### Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

### 2. Solution Explanation:
----------------------------
Maintain a double ended queue with a size of "self.k"
Maintain a cumulative sum that keeps track of sum of element in the queue.
When queue size is less than "self.k"
1. Add new element to the queue till it has reach size "self.k"
2. Add value of the element to cumulative sum
3. Return the : cumulative sum/size of the queue
Whenever a new element arrives when queue has reached size "self.k" then do following:
1. pop the first element from queue
2. Add new element to the queue
3. Subtract value of first popped element from cumulative sum and add value of the new element to cumulative sum.
4. Return : cumulative sum/ size of the queue

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(N)
"""
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.k = size
        self.cum_sum = 0
        self.queue = deque([])

    def next(self, val: int) -> float:
        if len(self.queue)<self.k:
            self.queue.appendleft(val)
            self.cum_sum += val
        else:
            first_val = self.queue.pop()
            self.queue.appendleft(val)
            self.cum_sum = self.cum_sum - first_val + val

        return self.cum_sum/len(self.queue)