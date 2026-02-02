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
        window = [] # Use as Monotonic Stack in increasing order height

        for i in range(len(heights)):
            while window and heights[window[-1]] >= heights[i]:
                ryt_exc_bound = i
                height = heights[window.pop()]

                if window: left_exc_bound = window[-1]
                else: left_exc_bound = -1

                width = dist = ryt_exc_bound - left_exc_bound - 1
                area = max(area, height * width)

            window.append(i)

        return area
