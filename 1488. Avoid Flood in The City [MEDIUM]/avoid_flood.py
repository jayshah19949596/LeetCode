from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last_rain = {}  # Map: lake -> last day it rained on that lake
        dry_days = []  # List of indices of days where rains[i] == 0 (dry days)
        result = [-1] * len(rains)

        for day, lake in enumerate(rains):

            if lake == 0:
                dry_days.append(day)
                result[day] = 1  # Temporarily assign any lake (1) for now

            else:

                # If this lake has rained before, it means the lake is full
                # We must dry it before it rains again to avoid flood
                if lake in last_rain:

                    # Find the earliest dry day AFTER the previous rain
                    # bisect_right finds the first index greater than last_rain[lake]
                    idx = bisect_right(dry_days, last_rain[lake])

                    # If no such dry day exists, flooding is unavoidable
                    if idx == len(dry_days): return []

                    # Use that dry day to dry this lake
                    dry_day = dry_days[idx]
                    result[dry_day] = lake
                    # Remove that dry day because it is now used
                    dry_days.pop(idx)

                last_rain[lake] = day  # Update the last rain day for this lake
                result[day] = -1  # Rain days must be -1 in the output

        return result
