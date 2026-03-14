"""
Approach: Greedy + min-heap

Why greedy works
If multiple events are available on some day, attending the one with the smallest end day is safest, because it may disappear sooner.

Working explanation
I sort events by start day, then sweep day by day. For each day, I push all events starting that day into a min-heap keyed by end day. 
I remove expired events, and if any event is available, I attend the one ending earliest. 
This greedy choice maximizes room for future events.

Time: O(n log n + D)
Space: O(n)
"""
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        total_events = len(events)
        last_day = max(event[1] for event in events)
        events.sort()  # sort by start day
        first_day = events[0][0]

        min_heap = []   # stores event end days
        events_attended = 0
        event_index = 0

        for current_day in range(first_day, last_day + 1):

            # add events that start on or before current_day
            while event_index < total_events and events[event_index][0] <= current_day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1

            # remove events that already expired
            while min_heap and min_heap[0] < current_day:
                heapq.heappop(min_heap)

            # attend the event that ends earliest
            if min_heap:
                heapq.heappop(min_heap)
                events_attended += 1

        return events_attended
