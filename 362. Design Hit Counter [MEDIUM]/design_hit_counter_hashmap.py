"""
362. Design Hit Counter [MEDIUM]
https://leetcode.com/problems/design-hit-counter/

### 1. Question Explanation:
----------------------------
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

#### Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

###  Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""
from collections import defaultdict


class HitCounter:

    def __init__(self):
        self.last_ts = 0
        self.hits = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        temp_del_hits = set([])
        if self.last_ts<timestamp-300:
            for ts in self.hits:
                if ts<timestamp-300:
                    temp_del_hits.add(ts)
        for ts in temp_del_hits:
            del self.hits[ts]

        self.last_ts = timestamp
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for ts in self.hits:
            if max(0, timestamp-300+1)<=ts<timestamp+1:
                total += self.hits[ts]
        return total
