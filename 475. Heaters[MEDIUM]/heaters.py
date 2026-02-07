"""
https://leetcode.com/problems/heaters/solutions/6655429/master-binary-search-to-find-minimum-hea-6ou8/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days


1. Sort both houses and heaters arrays.
2. For each house, binary search the position in heaters to find the closest heater.
3. Track the max of these minimum distances — that's the answer.

"""
"""
https://leetcode.com/problems/heaters/solutions/6655429/master-binary-search-to-find-minimum-hea-6ou8/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days


1. Sort both houses and heaters arrays.
2. For each house, binary search the position in heaters to find the closest heater.
3. Track the max of these minimum distances — that's the answer.

"""
class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        radius = 0
        for house in houses:
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            # distance from heater at left index
            dist = abs(heaters[left] - house) 
            if left > 0:
                # distance from heater at left-1 index
                dist = min(dist, abs(heaters[left - 1] - house))
            radius = max(radius, dist)
        return radius
