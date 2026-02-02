class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        heights.append(0)
        area = 0
        window = []

        for i in range(len(heights)):
            while window and heights[window[-1]] >= heights[i]:
                ryt_exc_bound = i
                height = heights[window.pop()]

                if window: left_exc_bound = window[-1]
                else: left_exc_bound = -1

                dist = ryt_exc_bound - left_exc_bound - 1
                area = max(area, height * dist)

            window.append(i)

        return area
