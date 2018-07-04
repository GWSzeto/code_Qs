# 84. Largest Rectangle in Histogram
class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        total = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                total = max(total, height * width)
            stack.append(i)
        
        return total
