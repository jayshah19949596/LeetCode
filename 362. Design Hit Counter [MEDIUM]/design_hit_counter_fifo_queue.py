"""
348. Design Tic-Tac-Toe [MEDIUM]
https://leetcode.com/problems/design-tic-tac-toe

### 1. Question Explanation:
----------------------------
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

### 2. Solution Explanation:
----------------------------
We maintain a queue for this problem. The init and hit (append) method are quite straightforward.
The main operation is performed in getHits.
In getHits, we keep popping elements from the queue (while queue exists), only if the difference
between the current timestamp and the first element of the queue is greater than or equal to 300.
What this does is that the queue would remove all elements that have timestamp difference of more
than or equal to 300. What we are left is the queue with the closest 300 timestamps to the current
timestamp. If we encounter a difference of less than 300, then this operation stops. Finally, the
length of the queue is the number of "hits" at the current timestamp.

###  Complexity Analysis:
----------------------------
Time Complexity: O(1)
Space Complexity: O(N)
"""
from collections import deque


class HitCounter:
    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()

        return len(self.queue)
