"""
981. Time Based Key-Value Store [MEDIUM]
https://leetcode.com/problems/time-based-key-value-store

### 1. Question Explanation:
----------------------------
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
1. TimeMap() Initializes the object of the data structure.
2. void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
3. String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

### 2. Solution Explanation:
----------------------------
Approach: Sorted Map + Binary Search
Intuition
If the timestamps in the inner map were sorted, then we can use binary search to find the target time more efficiently.
Thus, we can use a sorted map as values to the Hashmap.
A sorted map keeps the stored key-value pairs sorted based on the key.
So now our data structure keyTimeMap will look like: HashMap(key, SortedMap(timestamp, value)).
"""
from sortedcontainers import SortedDict
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Time : O(L*LogN)
            Where L is height of the tree and N is number of "key" in SortedDict i.e. len(SortedDict)
            Because SortedDict internal implementation is kind of balanced binary tree and in worst case we might have
            to compare LogN nodes (height of tree) of length L each with argument key.
        Space: O(M+N)
            Where M is number of key
            Where N is total number of timestamp
        """
        self.timemap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        """
        Time : O(L*LogN)
            Where N is length of sorted_dict i.e. total number of timestamps
            and L is height of tree
        Space: O(M+N)
            Where M is number of key
            Where N is total number of timestamp
        """

        sorted_dict = self.timemap[key]
        if timestamp in sorted_dict:
            return sorted_dict[timestamp]
        sorted_list = sorted_dict._list
        idx_to_insert = sorted_list.bisect_left(timestamp)
        if idx_to_insert == 0: return ""
        res_key = sorted_list[idx_to_insert - 1]
        return sorted_dict[res_key]
