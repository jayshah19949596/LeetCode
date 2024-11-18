"""
https://leetcode.com/problems/meeting-rooms-ii/

### 1. Question Explanation:
----------------------------
Given an array of meeting time intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

"""
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return self.sorting_two_ptr(intervals)
        # return self.sort_with_heap(intervals)

    def sorting_two_ptr(self, intervals: List[List[int]]) -> int:
        """
        1. Separate out the start times and the end times in their separate arrays.
        2. Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.
        3. We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
        4. When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. If this is the case then that would mean some meeting has ended by the time the meeting at "s_ptr" had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
        5. If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment "e_ptr".
        6. Repeat this process until "s_ptr" processes all of the meetings.

        Time Complexity - O(N.LogN)
        Space Complexity - O(N)
        """
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0]), ends.append(interval[1])
        starts, ends = sorted(starts), sorted(ends)
        max_room = rooms = s_ptr = e_ptr = 0
        while s_ptr < len(starts) and e_ptr < len(ends):
            if starts[s_ptr] < ends[e_ptr]:
                rooms, s_ptr = rooms+1, s_ptr+1
            else:
                rooms, e_ptr = rooms-1, e_ptr+1
            max_room = max(max_room, rooms)
        return max_room

    def sort_with_prirority_queue(self, intervals: List[List[int]]) -> int:
        """
        1. Sort the given meetings by their start time.
        2. Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
        3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
        4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
        5. If not, then we allocate a new room and add it to the heap.
        6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

        Time Complexity - O(N.LogN)
        Space Complexity - O(N)
        """
        intervals.sort(key=lambda x: x[0])
        max_room, rooms = 0, []
        for i in range(len(intervals)):
            while rooms and rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
            max_room = max(max_room, len(rooms))
        return max_room
