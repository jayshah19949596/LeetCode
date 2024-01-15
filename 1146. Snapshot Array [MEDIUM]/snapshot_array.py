"""
1146. Snapshot Array [MEDIUM]
https://leetcode.com/problems/snapshot-array/

### 1. Question Explanation:
----------------------------
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.
Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

### 2. Solution:
----------------------------
For each index of the array, store the historical values as [snap_id, value].
When setting a value, append a new [snap_id, value] if the value and id has changed.
Binary search the history to find a value at a previous snap.

### 3. Complexity Analysis:
----------------------------
Time -  O(n) for __init__ when n is the array length.
        O(1) for set and snap.
        O(m) for get for m snap operations.
Space - O(mn)
"""
import bisect


class SnapshotArray:
    def __init__(self, length: int):
        # self.history = [[index[snap_id, value]]]
        # snap_id = -1, value at that snap_id "-1" for the ith index  = 0
        self.history = [[[-1, 0]] for _ in range(length)]
        self.id = 0  # next snap id

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.id:  # update value only if id is unchanged
            self.history[index][-1][1] = val
        else:
            self.history[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_left(self.history[index], [snap_id, float("inf")])
        return self.history[index][i - 1][1]
